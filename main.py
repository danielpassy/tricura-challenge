import csv
import json
import re
from dataclasses import dataclass
from datetime import datetime, date
from pathlib import Path

SESSIONS_DIR = Path("challenge-assets/macro_data_refinement/quarterly_output/sessions")

VALID_DEPARTMENTS = {"MDR", "SA", "WB"}
VALID_PROCESSORS = {
    "James.L",
    "Nora.K",
    "Arthur.B",
    "Lena.P",
    "Felix.G",
    "Dr.Voss",
    "Clara.M",
}
VALID_BINS = {"GR", "BL", "AX", "SP"}
VALID_CATEGORIES = {"alpha", "beta", "gamma", "delta"}
Q4_START = datetime(2025, 10, 1)
Q4_END = datetime(2025, 12, 31, 23, 59, 59)

# Hidden compliance annex (revealed via JANSKY gate)
DEPT_BIN_MATRIX = {"MDR": {"GR", "BL", "AX"}, "SA": {"SP", "BL"}, "WB": {"GR", "AX"}}
NORAK_TERMINATION = date(2025, 11, 15)
VALUE_CAP = 1000.00


@dataclass
class Entry:
    ref: str | None
    bin: str
    category: str
    value_raw: object  # may be str (csv/txt) or number (mdr) or None


@dataclass
class Session:
    session_id: str
    department: str
    processor: str
    timestamp_raw: str
    entries: list[Entry]
    path: Path
    timestamp: datetime | None = None  # populated after parse


def parse_timestamp(ts: str) -> datetime:
    for fmt in ("%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.strptime(ts.strip(), fmt)
        except ValueError:
            continue
    raise ValueError(f"Invalid timestamp: {ts}")


# ---------------------------------------------------------------------------
# Compliance rules
#
# All twelve rules listed in canonical order: public 1..6 then hidden 1..6.
# Each rule takes a Ctx and returns an error message, or None if it passes.
# Rules 8 and 9 are merged into the dept/bin matrix rule.
# Rule 11 (unique session_id) is enforced in dedupe_sessions, not here.
# ---------------------------------------------------------------------------


@dataclass
class Ctx:
    session: Session
    entry: Entry | None = None
    value: float | None = None


def rule_p1_department(ctx: Ctx) -> str | None:
    """P1: department must be MDR, SA, or WB."""
    if ctx.session.department not in VALID_DEPARTMENTS:
        return f"invalid department: {ctx.session.department!r}"
    return None


def rule_p2_processor(ctx: Ctx) -> str | None:
    """P2: processor must be in the directory."""
    if ctx.session.processor not in VALID_PROCESSORS:
        return f"invalid processor: {ctx.session.processor!r}"
    return None


def rule_p3_bin(ctx: Ctx) -> str | None:
    """P3: bin must be one of the four signals."""
    if ctx.entry.bin not in VALID_BINS:
        return f"invalid bin: {ctx.entry.bin!r}"
    return None


def rule_p4_category(ctx: Ctx) -> str | None:
    """P4: category must be alpha/beta/gamma/delta (case-sensitive)."""
    if ctx.entry.category not in VALID_CATEGORIES:
        return f"invalid category: {ctx.entry.category!r}"
    return None


def rule_p5_value_positive(ctx: Ctx) -> str | None:
    """P5: value must be positive."""
    if ctx.value <= 0:
        return f"invalid value: {ctx.value}"
    return None


def rule_p6_q4_2025(ctx: Ctx) -> str | None:
    """P6: timestamp must fall within Q4 2025."""
    if not (Q4_START <= ctx.session.timestamp <= Q4_END):
        return f"timestamp outside Q4 2025: {ctx.session.timestamp}"
    return None


def rule_h1_norak_terminated(ctx: Ctx) -> str | None:
    """7: Nora.K entries after 2025-11-15 are invalid."""
    if ctx.session.processor == "Nora.K" and ctx.session.timestamp.date() > NORAK_TERMINATION:
        return f"Nora.K terminated after {NORAK_TERMINATION}"
    return None


def rule_h23_dept_bin_matrix(ctx: Ctx) -> str | None:
    """8/9: bin must match the department's authorized set."""
    dept = ctx.session.department
    bin_ = ctx.entry.bin
    if dept in DEPT_BIN_MATRIX and bin_ in VALID_BINS:
        if bin_ not in DEPT_BIN_MATRIX[dept]:
            return f"bin {bin_} not allowed for dept {dept}"
    return None


def rule_h4_value_cap(ctx: Ctx) -> str | None:
    """10: value must be below 1000.00."""
    if ctx.value >= VALUE_CAP:
        return f"value >= {VALUE_CAP}: {ctx.value}"
    return None


def rule_h6_weekday_only(ctx: Ctx) -> str | None:
    """12: only Monday-Friday sessions are valid."""
    if ctx.session.timestamp.weekday() >= 5:
        return f"weekend timestamp: {ctx.session.timestamp}"
    return None


# Pipelines: which rules apply at the session level vs. per-entry, in canonical order.
SESSION_RULES = [
    ("P1", rule_p1_department),
    ("P2", rule_p2_processor),
    ("P6", rule_p6_q4_2025),
    ("7", rule_h1_norak_terminated),
    ("12", rule_h6_weekday_only),
]

ENTRY_RULES = [
    ("P3", rule_p3_bin),
    ("P4", rule_p4_category),
    ("P5", rule_p5_value_positive),
    ("8/9", rule_h23_dept_bin_matrix),
    ("10", rule_h4_value_cap),
]


def validate_session(s: Session) -> list[str]:
    ctx = Ctx(session=s)
    return [f"{label}: {err}" for label, rule in SESSION_RULES if (err := rule(ctx)) is not None]


def validate_entry(s: Session, e: Entry, value: float) -> list[str]:
    ctx = Ctx(session=s, entry=e, value=value)
    return [f"{label}: {err}" for label, rule in ENTRY_RULES if (err := rule(ctx)) is not None]


def load_csv(path: Path) -> Session | None:
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        return None
    first = rows[0]
    return Session(
        session_id=first["session_id"],
        department=first["department"],
        processor=first["processor"],
        timestamp_raw=first["timestamp"],
        entries=[
            Entry(
                ref=r.get("ref"),
                bin=r["bin"],
                category=r["classification"],
                value_raw=r.get("output_metric"),
            )
            for r in rows
        ],
        path=path,
    )


def load_txt(path: Path) -> Session | None:
    text = path.read_text(encoding="utf-8")
    header: dict[str, str] = {}
    entries: list[Entry] = []
    for line in text.strip().splitlines():
        if line.startswith("---"):
            continue
        if "|" in line:
            parts = {
                k.strip(): v.strip()
                for k, v in (p.split(":", 1) for p in line.split("|") if ":" in p)
            }
            entries.append(
                Entry(
                    ref=parts.get("REF"),
                    bin=parts.get("BIN", ""),
                    category=parts.get("TYPE", ""),
                    value_raw=parts.get("READING", ""),
                )
            )
        else:
            m = re.match(r"^(\w+):\s*(.+)$", line)
            if m:
                header[m.group(1)] = m.group(2).strip()
    return Session(
        session_id=header.get("SESSION", ""),
        department=header.get("DEPARTMENT", ""),
        processor=header.get("PROCESSOR", ""),
        timestamp_raw=header.get("TIMESTAMP", ""),
        entries=entries,
        path=path,
    )


def load_mdr(path: Path) -> Session | None:
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return Session(
        session_id=data.get("session_id", ""),
        department=data.get("department", ""),
        processor=data.get("processor", ""),
        timestamp_raw=data.get("timestamp", ""),
        entries=[
            Entry(
                ref=e.get("ref"),
                bin=e.get("bin", ""),
                category=e.get("category", ""),
                value_raw=e.get("value"),
            )
            for e in data.get("entries", [])
        ],
        path=path,
    )


LOADERS = {".csv": load_csv, ".txt": load_txt, ".mdr": load_mdr}


def collect_sessions() -> list[Session]:
    sessions: list[Session] = []
    for folder in SESSIONS_DIR.iterdir():
        for path in sorted(folder.iterdir()):
            loader = LOADERS.get(path.suffix)
            if loader:
                s = loader(path)
                if s:
                    sessions.append(s)
    return sessions


def dedupe_sessions(sessions: list[Session]) -> tuple[list[Session], list[str]]:
    """Hidden rule 5: keep only earliest timestamp per session_id."""
    by_id: dict[str, Session] = {}
    anomalies: list[str] = []
    for s in sessions:
        try:
            s.timestamp = parse_timestamp(s.timestamp_raw)
        except ValueError as e:
            anomalies.append(f"{s.path.name}: parse error: {e}")
            continue
        existing = by_id.get(s.session_id)
        if existing is None:
            by_id[s.session_id] = s
        elif s.timestamp < existing.timestamp:
            anomalies.append(
                f"11: duplicate session_id {s.session_id}: discarding {existing.path.name} "
                f"and keeping {s.path.name} (earlier)"
            )
            by_id[s.session_id] = s
        else:
            anomalies.append(
                f"11: duplicate session_id {s.session_id}: discarding {s.path.name} "
                f"(later than {existing.path.name})"
            )
    return list(by_id.values()), anomalies


def process_session(s: Session) -> tuple[float, list[str]]:
    total = 0.0
    anomalies: list[str] = []
    name = s.path.name
    session_errors = validate_session(s)
    if session_errors:
        anomalies.append(f"{name} (session): {'; '.join(session_errors)}")
        return 0.0, anomalies

    for entry in s.entries:
        try:
            value = float(entry.value_raw)
        except (TypeError, ValueError):
            anomalies.append(f"{name} ref={entry.ref}: non-numeric value")
            continue
        errs = validate_entry(s, entry, value)
        if errs:
            anomalies.append(f"{name} ref={entry.ref}: {'; '.join(errs)}")
        else:
            total += value
    return total, anomalies


def main():
    sessions = collect_sessions()
    sessions, dedupe_anomalies = dedupe_sessions(sessions)

    grand_total = 0.0
    all_anomalies = list(dedupe_anomalies)
    for s in sessions:
        total, anomalies = process_session(s)
        grand_total += total
        all_anomalies.extend(anomalies)

    print(f"Sessions considered (after dedupe): {len(sessions)}")
    print(f"Anomalies found: {len(all_anomalies)}")
    for a in all_anomalies:
        print(f"  ⚠ {a}")
    print(f"\nTotal sum of valid entries: {grand_total:.2f}")


if __name__ == "__main__":
    main()
