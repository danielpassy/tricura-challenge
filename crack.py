"""Brute-force the SHA-256 access gate from compliance.html.

The gate validates input client-side via:
    SHA-256(input.trim().toUpperCase()) == H

Since the validator runs offline (no rate limit), we can crack short codes
locally. Charset is restricted to [A-Z0-9] because the JS uppercases input.
"""
import hashlib
import itertools
import multiprocessing as mp
import string
import time

TARGET = bytes.fromhex("38b19f2e76c9fa1e3ab74c80fb3e95b3cd761ce39b0e2359b6ac15e012220907")
SUFFIX = "arturic"
CHARSET = (string.ascii_uppercase + string.digits).encode()


def worker(args):
    length, prefix_byte = args
    rest_len = length - 1
    if rest_len == 0:
        s = bytes([prefix_byte])
        return s.decode() if hashlib.sha256(s).digest() == TARGET else None
    for tail in itertools.product(CHARSET, repeat=rest_len):
        s = bytes([prefix_byte]) + bytes(tail)
        if hashlib.sha256(s).digest() == TARGET:
            return s.decode()
    return None


def main():
    length = 1
    while True:
        t = time.time()
        tasks = [(length, c) for c in CHARSET]
        with mp.Pool(processes=mp.cpu_count()) as pool:
            for res in pool.imap_unordered(worker, tasks):
                if res:
                    elapsed = time.time() - t
                    print(f"\n*** MATCH (len={length}, {elapsed:.1f}s): {res!r} ***")
                    url_hash = hashlib.sha256((res + SUFFIX).encode()).hexdigest()
                    print(f"Hidden URL: {url_hash}.html")
                    return
        elapsed = time.time() - t
        rate = (len(CHARSET) ** length) / elapsed if elapsed > 0 else 0
        print(f"len={length} done in {elapsed:.1f}s ({rate/1e6:.1f}M h/s) — no match")
        length += 1


if __name__ == "__main__":
    main()
