# Tricura Challenge, Macro Data Refinement

This is the project from the Tricura selection process.
To reproduce the result, just run `python main.py`.

The deliverables required by the project are:
- A git repository with your code.
- The final sum: `1023118.20`
- A brief explanation (~400 words) of your methodology and any anomalies you encountered.


## Explanation
I started from the portal rules in the challenge materials, then started investigating the hidden annex behind the access-code gate.
I tried to figure out the password logically, doing a Google image search on `facility_exterior.png`.
I arrived at Bell Labs Holmdel Complex.
I tried many strings against the hash. Nothing matched.
Then I realized it was client-side and tried to brute force it. The code is in `crack.py`.
That found `JANSKY` and opened the extra compliance rules.
After that I ran `main.py` over the quarterly files and checked the full set of rules: public validation, the `Nora.K` cutoff, the dept/bin matrix, the value cap, dedupe by earliest `session_id`, and weekdays only.
Most of the bad rows were what you would expect from that setup: duplicate sessions, weekend timestamps, Q4 dates outside the window, invalid departments or processors, wrong bins for the department, bad categories, negative values, and a few values at or above `1000.00`.
There were also some non-numeric readings.
After dedupe and validation, the final sum was `1023118.20`.


## Anomalies

The number shows which rule it did not comply with. Duplicate session warnings show the file name and the rule number.

Sessions considered (after dedupe): 400
Anomalies found: 521
- SA-0046.csv: 11: duplicate session_id SA-0046: discarding SA-0046.csv (later than SA-0046.csv)
- WB-0007.txt: 11: duplicate session_id WB-0007: discarding WB-0007.txt and keeping WB-0007.txt (earlier)
- MDR-0018.mdr: 11: duplicate session_id MDR-0018: discarding MDR-0018.mdr and keeping MDR-0018.mdr (earlier)
- MDR-0025.mdr: 11: duplicate session_id MDR-0025: discarding MDR-0025.mdr and keeping MDR-0025.mdr (earlier)
- MDR-0070.mdr: 11: duplicate session_id MDR-0070: discarding MDR-0070.mdr and keeping MDR-0070.mdr (earlier)
- MDR-0081.mdr: 11: duplicate session_id MDR-0081: discarding MDR-0081.mdr and keeping MDR-0081.mdr (earlier)
- MDR-0094.mdr: 11: duplicate session_id MDR-0094: discarding MDR-0094.mdr and keeping MDR-0094.mdr (earlier)
- MDR-0098.mdr: 11: duplicate session_id MDR-0098: discarding MDR-0098.mdr and keeping MDR-0098.mdr (earlier)
- MDR-0100.mdr: 11: duplicate session_id MDR-0100: discarding MDR-0100.mdr and keeping MDR-0100.mdr (earlier)
- MDR-0105.mdr: 11: duplicate session_id MDR-0105: discarding MDR-0105.mdr and keeping MDR-0105.mdr (earlier)
- MDR-0128.mdr: 11: duplicate session_id MDR-0128: discarding MDR-0128.mdr and keeping MDR-0128.mdr (earlier)
- MDR-0136.mdr: 11: duplicate session_id MDR-0136: discarding MDR-0136.mdr and keeping MDR-0136.mdr (earlier)
- MDR-0150.mdr: 11: duplicate session_id MDR-0150: discarding MDR-0150.mdr and keeping MDR-0150.mdr (earlier)
- MDR-0152.mdr: 11: duplicate session_id MDR-0152: discarding MDR-0152.mdr and keeping MDR-0152.mdr (earlier)
- MDR-0159.mdr: 11: duplicate session_id MDR-0159: discarding MDR-0159.mdr and keeping MDR-0159.mdr (earlier)
- SA-0066.csv (session): 12: weekend timestamp: 2025-12-21 10:28:00
- SA-0068.csv (session): P6: timestamp outside Q4 2025: 2026-01-29 11:00:00
- SA-0070.csv (session): P2: invalid processor: 'Cross.R'
- SA-0071.csv (session): 12: weekend timestamp: 2025-10-11 09:05:00
- SA-0073.csv (session): P6: timestamp outside Q4 2025: 2026-01-29 09:00:00
- SA-0074.csv (session): P6: timestamp outside Q4 2025: 2025-09-01 11:00:00
- SA-0075.csv (session): 12: weekend timestamp: 2025-12-07 11:02:00
- SA-0076.csv (session): 12: weekend timestamp: 2025-12-28 16:40:00
- SA-0079.csv (session): P2: invalid processor: 'Harmon.D'
- SA-0082.csv (session): P2: invalid processor: 'Webb.T'
- SA-0086.csv ref=SP-E425: P5: invalid value: -441.06
- SA-0086.csv ref=XX-E430: P3: invalid bin: 'XX'
- SA-0086.csv ref=SP-E431: P4: invalid category: 'omega'
- SA-0086.csv ref=SP-E435: 10: value >= 1000.0: 1785.08
- SA-0087.csv ref=SP-E439: P4: invalid category: 'omega'
- SA-0087.csv ref=SP-E441: non-numeric value
- SA-0087.csv ref=SP-E443: P4: invalid category: 'omega'
- SA-0088.csv ref=XX-E446: P3: invalid bin: 'XX'
- SA-0088.csv ref=SP-E447: P4: invalid category: 'zeta'
- SA-0088.csv ref=SP-E449: non-numeric value
- SA-0088.csv ref=SP-E453: 10: value >= 1000.0: 1161.53
- SA-0088.csv ref=SP-E455: 10: value >= 1000.0: 1354.75
- SA-0089.csv ref=XX-E464: P3: invalid bin: 'XX'
- SA-0090.csv ref=SP-E471: P5: invalid value: -393.06
- SA-0090.csv ref=SP-E472: 10: value >= 1000.0: 4288.15
- SA-0090.csv ref=SP-E473: P5: invalid value: -121.18
- SA-0090.csv ref=NV-E477: P3: invalid bin: 'NV'
- SA-0090.csv ref=ZZ-E483: P3: invalid bin: 'ZZ'
- SA-0091.csv ref=BL-E488: P5: invalid value: -58.82
- SA-0091.csv ref=SP-E492: P4: invalid category: 'omega'
- SA-0091.csv ref=SP-E493: P5: invalid value: -377.81
- SA-0091.csv ref=SP-E495: 10: value >= 1000.0: 4666.69
- SA-0091.csv ref=XX-E498: P3: invalid bin: 'XX'
- SA-0091.csv ref=BL-E500: P5: invalid value: -206.73
- SA-0091.csv ref=BL-E503: 10: value >= 1000.0: 4735.11
- SA-0092.csv ref=SP-E504: 10: value >= 1000.0: 1950.59
- SA-0092.csv ref=SP-E511: P4: invalid category: 'epsilon'
- SA-0092.csv ref=SP-E516: 10: value >= 1000.0: 4120.97
- SA-0092.csv ref=BL-E517: P4: invalid category: 'zeta'
- SA-0092.csv ref=BL-E518: P4: invalid category: 'omega'
- SA-0092.csv ref=BL-E519: 10: value >= 1000.0: 3422.73
- SA-0092.csv ref=SP-E520: 10: value >= 1000.0: 3296.35
- SA-0093.csv ref=BL-E525: non-numeric value
- SA-0093.csv ref=BL-E527: P4: invalid category: 'zeta'
- SA-0093.csv ref=NV-E530: P3: invalid bin: 'NV'
- SA-0093.csv ref=BL-E531: P4: invalid category: 'sigma'
- SA-0093.csv ref=BL-E532: non-numeric value
- SA-0094.csv ref=SP-E534: non-numeric value
- SA-0094.csv ref=BL-E540: P4: invalid category: 'sigma'
- SA-0094.csv ref=SP-E545: P5: invalid value: -92.85
- SA-0094.csv ref=XX-E547: P3: invalid bin: 'XX'
- SA-0095.csv ref=BL-E551: 10: value >= 1000.0: 2762.6
- SA-0095.csv ref=SP-E558: P4: invalid category: 'omega'
- SA-0095.csv ref=SP-E560: P5: invalid value: -267.88
- SA-0095.csv ref=SP-E561: P4: invalid category: 'omega'
- SA-0095.csv ref=ZZ-E566: P3: invalid bin: 'ZZ'
- SA-0096.csv ref=XX-E568: P3: invalid bin: 'XX'
- SA-0096.csv ref=BL-E573: P4: invalid category: 'sigma'
- SA-0097.csv ref=BL-E583: 10: value >= 1000.0: 4968.6
- SA-0097.csv ref=SP-E587: non-numeric value
- SA-0097.csv ref=BL-E589: non-numeric value
- SA-0097.csv ref=NV-E591: P3: invalid bin: 'NV'
- SA-0097.csv ref=BL-E595: non-numeric value
- SA-0097.csv ref=SP-E596: P4: invalid category: 'zeta'
- SA-0099.csv ref=SP-E606: non-numeric value
- SA-0099.csv ref=BL-E607: P4: invalid category: 'sigma'
- SA-0099.csv ref=BL-E608: non-numeric value
- SA-0099.csv ref=BL-E611: P4: invalid category: 'sigma'
- SA-0099.csv ref=BL-E613: 10: value >= 1000.0: 2614.61
- SA-0099.csv ref=SP-E615: non-numeric value
- SA-0099.csv ref=SP-E619: 10: value >= 1000.0: 4705.27
- SA-0099.csv ref=BL-E620: P5: invalid value: -239.23
- SA-0099.csv ref=SP-E622: 10: value >= 1000.0: 2300.98
- SA-0100.csv ref=BL-E623: P4: invalid category: 'zeta'
- SA-0100.csv ref=NV-E628: P3: invalid bin: 'NV'
- SA-0100.csv ref=SP-E631: P4: invalid category: 'zeta'
- SA-0100.csv ref=BL-E632: P4: invalid category: 'zeta'
- SA-0100.csv ref=BL-E633: 10: value >= 1000.0: 3155.66
- SA-0100.csv ref=SP-E634: P4: invalid category: 'epsilon'
- MDR-0182.mdr ref=SP-C455: 8/9: bin SP not allowed for dept WB
- MDR-0182.mdr ref=SP-C456: 8/9: bin SP not allowed for dept WB
- MDR-0182.mdr ref=SP-C457: 8/9: bin SP not allowed for dept WB
- MDR-0182.mdr ref=SP-C458: 8/9: bin SP not allowed for dept WB
- MDR-0182.mdr ref=SP-C459: 8/9: bin SP not allowed for dept WB
- MDR-0182.mdr ref=SP-C460: 8/9: bin SP not allowed for dept WB
- MDR-0182.mdr ref=SP-C461: 8/9: bin SP not allowed for dept WB
- MDR-0182.mdr ref=SP-C462: 8/9: bin SP not allowed for dept WB
- MDR-0182.mdr ref=SP-C463: 8/9: bin SP not allowed for dept WB
- MDR-0182.mdr ref=SP-C464: 8/9: bin SP not allowed for dept WB
- MDR-0182.mdr ref=SP-C465: 8/9: bin SP not allowed for dept WB
- MDR-0182.mdr ref=SP-C466: 8/9: bin SP not allowed for dept WB
- MDR-0182.mdr ref=SP-C467: 8/9: bin SP not allowed for dept WB
- MDR-0182.mdr ref=SP-C468: 8/9: bin SP not allowed for dept WB
- MDR-0182.mdr ref=SP-C469: 8/9: bin SP not allowed for dept WB
- MDR-0182.mdr ref=SP-C470: 8/9: bin SP not allowed for dept WB
- MDR-0182.mdr ref=SP-C471: 8/9: bin SP not allowed for dept WB
- MDR-0207.mdr ref=SP-C752: 8/9: bin SP not allowed for dept WB
- MDR-0207.mdr ref=SP-C753: 8/9: bin SP not allowed for dept WB
- MDR-0207.mdr ref=SP-C754: 8/9: bin SP not allowed for dept WB
- MDR-0207.mdr ref=SP-C755: 8/9: bin SP not allowed for dept WB
- MDR-0207.mdr ref=SP-C756: 8/9: bin SP not allowed for dept WB
- MDR-0207.mdr ref=SP-C757: 8/9: bin SP not allowed for dept WB
- MDR-0207.mdr ref=SP-C758: 8/9: bin SP not allowed for dept WB
- MDR-0207.mdr ref=SP-C759: 8/9: bin SP not allowed for dept WB
- MDR-0207.mdr ref=SP-C760: 8/9: bin SP not allowed for dept WB
- MDR-0209.mdr ref=SP-C774: 8/9: bin SP not allowed for dept WB
- MDR-0209.mdr ref=SP-C775: 8/9: bin SP not allowed for dept WB
- MDR-0209.mdr ref=SP-C776: 8/9: bin SP not allowed for dept WB
- MDR-0209.mdr ref=SP-C777: 8/9: bin SP not allowed for dept WB
- MDR-0209.mdr ref=SP-C778: 8/9: bin SP not allowed for dept WB
- MDR-0209.mdr ref=SP-C779: 8/9: bin SP not allowed for dept WB
- MDR-0209.mdr ref=SP-C780: 8/9: bin SP not allowed for dept WB
- MDR-0209.mdr ref=SP-C781: 8/9: bin SP not allowed for dept WB
- MDR-0209.mdr ref=SP-C782: 8/9: bin SP not allowed for dept WB
- MDR-0209.mdr ref=SP-C783: 8/9: bin SP not allowed for dept WB
- MDR-0209.mdr ref=SP-C784: 8/9: bin SP not allowed for dept WB
- MDR-0209.mdr ref=SP-C785: 8/9: bin SP not allowed for dept WB
- MDR-0209.mdr ref=SP-C786: 8/9: bin SP not allowed for dept WB
- MDR-0209.mdr ref=SP-C787: 8/9: bin SP not allowed for dept WB
- MDR-0209.mdr ref=SP-C788: 8/9: bin SP not allowed for dept WB
- MDR-0209.mdr ref=SP-C789: 8/9: bin SP not allowed for dept WB
- MDR-0209.mdr ref=SP-C790: 8/9: bin SP not allowed for dept WB
- MDR-0209.mdr ref=SP-C791: 8/9: bin SP not allowed for dept WB
- MDR-0209.mdr ref=SP-C792: 8/9: bin SP not allowed for dept WB
- WB-0034.txt (session): P2: invalid processor: 'Harmon.D'
- WB-0035.txt (session): P2: invalid processor: 'Blake.S'
- WB-0038.txt (session): P2: invalid processor: 'Harmon.D'
- WB-0039.txt (session): P6: timestamp outside Q4 2025: 2026-01-29 15:00:00
- WB-0040.txt (session): P6: timestamp outside Q4 2025: 2025-09-01 14:00:00
- WB-0042.txt (session): 12: weekend timestamp: 2025-10-18 10:46:00
- WB-0044.txt ref=AX-F161: 10: value >= 1000.0: 2763.9
- WB-0044.txt ref=AX-F165: P4: invalid category: 'omega'
- WB-0044.txt ref=AX-F166: P4: invalid category: 'sigma'
- WB-0044.txt ref=GR-F168: P4: invalid category: 'zeta'
- WB-0045.txt ref=AX-F170: non-numeric value
- WB-0045.txt ref=AX-F174: 10: value >= 1000.0: 4920.55
- WB-0045.txt ref=AX-F175: P5: invalid value: -250.32
- WB-0045.txt ref=AX-F181: P4: invalid category: 'omega'
- WB-0046.txt ref=GR-F182: P5: invalid value: -212.15
- WB-0046.txt ref=GR-F184: 10: value >= 1000.0: 2062.78
- WB-0046.txt ref=NV-F191: P3: invalid bin: 'NV'
- WB-0046.txt ref=AX-F194: non-numeric value
- WB-0047.txt ref=GR-F196: P5: invalid value: -178.6
- WB-0047.txt ref=ZZ-F198: P3: invalid bin: 'ZZ'
- WB-0047.txt ref=AX-F204: 10: value >= 1000.0: 1145.47
- WB-0048.txt ref=GR-F216: non-numeric value
- WB-0048.txt ref=GR-F217: P5: invalid value: -435.4
- WB-0048.txt ref=AX-F220: P4: invalid category: 'sigma'
- WB-0048.txt ref=ZZ-F223: P3: invalid bin: 'ZZ'
- WB-0049.txt ref=GR-F228: P4: invalid category: 'epsilon'
- WB-0049.txt ref=ZZ-F233: P3: invalid bin: 'ZZ'
- WB-0049.txt ref=PH-F235: P3: invalid bin: 'PH'
- WB-0049.txt ref=GR-F236: P4: invalid category: 'sigma'
- WB-0049.txt ref=NV-F239: P3: invalid bin: 'NV'
- WB-0049.txt ref=AX-F242: 10: value >= 1000.0: 2005.71
- WB-0049.txt ref=GR-F243: P4: invalid category: 'epsilon'
- WB-0050.txt ref=ZZ-F251: P3: invalid bin: 'ZZ'
- WB-0050.txt ref=AX-F254: P4: invalid category: 'sigma'
- WB-0050.txt ref=GR-F255: non-numeric value
- MDR-0156.mdr ref=GR-X042: P5: invalid value: 0.0
- MDR-0164.mdr (session): P6: timestamp outside Q4 2025: 2025-09-30 23:59:59
- MDR-0165.mdr (session): P1: invalid department: 'HR'
- MDR-0168.mdr (session): 7: Nora.K terminated after 2025-11-15; 12: weekend timestamp: 2025-11-16 00:00:00
- MDR-0169.mdr (session): P1: invalid department: 'TESTING'
- MDR-0171.mdr ref=AX-F292: 10: value >= 1000.0: 1000.0
- MDR-0172.mdr (session): P1: invalid department: 'QA'
- MDR-0173.mdr (session): P1: invalid department: 'HR'
- MDR-0174.mdr (session): P1: invalid department: 'HR'
- MDR-0176.mdr (session): 12: weekend timestamp: 2025-10-04 00:01:00
- MDR-0177.mdr (session): P1: invalid department: 'HR'
- MDR-0178.mdr (session): 7: Nora.K terminated after 2025-11-15
- MDR-0179.mdr ref=SP-C409: 8/9: bin SP not allowed for dept MDR
- MDR-0179.mdr ref=SP-C410: 8/9: bin SP not allowed for dept MDR
- MDR-0179.mdr ref=SP-C411: 8/9: bin SP not allowed for dept MDR
- MDR-0179.mdr ref=SP-C412: 8/9: bin SP not allowed for dept MDR
- MDR-0179.mdr ref=SP-C413: 8/9: bin SP not allowed for dept MDR
- MDR-0179.mdr ref=SP-C414: 8/9: bin SP not allowed for dept MDR
- MDR-0179.mdr ref=SP-C415: 8/9: bin SP not allowed for dept MDR
- MDR-0179.mdr ref=SP-C416: 8/9: bin SP not allowed for dept MDR
- MDR-0179.mdr ref=SP-C417: 8/9: bin SP not allowed for dept MDR
- MDR-0179.mdr ref=SP-C418: 8/9: bin SP not allowed for dept MDR
- MDR-0179.mdr ref=SP-C419: 8/9: bin SP not allowed for dept MDR
- MDR-0179.mdr ref=SP-C420: 8/9: bin SP not allowed for dept MDR
- MDR-0179.mdr ref=SP-C421: 8/9: bin SP not allowed for dept MDR
- MDR-0179.mdr ref=SP-C422: 8/9: bin SP not allowed for dept MDR
- MDR-0179.mdr ref=SP-C423: 8/9: bin SP not allowed for dept MDR
- MDR-0179.mdr ref=SP-C424: 8/9: bin SP not allowed for dept MDR
- MDR-0179.mdr ref=SP-C425: 8/9: bin SP not allowed for dept MDR
- MDR-0179.mdr ref=SP-C426: 8/9: bin SP not allowed for dept MDR
- MDR-0180.mdr (session): P6: timestamp outside Q4 2025: 2026-01-29 09:00:00; 7: Nora.K terminated after 2025-11-15
- MDR-0181.mdr (session): P6: timestamp outside Q4 2025: 2026-01-09 08:00:00; 7: Nora.K terminated after 2025-11-15
- MDR-0183.mdr (session): P6: timestamp outside Q4 2025: 2026-01-09 10:00:00
- MDR-0184.mdr (session): 7: Nora.K terminated after 2025-11-15
- MDR-0185.mdr (session): P6: timestamp outside Q4 2025: 2025-08-04 12:00:00
- MDR-0186.mdr ref=SP-C509: 8/9: bin SP not allowed for dept MDR
- MDR-0186.mdr ref=SP-C510: 8/9: bin SP not allowed for dept MDR
- MDR-0186.mdr ref=SP-C511: 8/9: bin SP not allowed for dept MDR
- MDR-0186.mdr ref=SP-C512: 8/9: bin SP not allowed for dept MDR
- MDR-0186.mdr ref=SP-C513: 8/9: bin SP not allowed for dept MDR
- MDR-0186.mdr ref=SP-C514: 8/9: bin SP not allowed for dept MDR
- MDR-0186.mdr ref=SP-C515: 8/9: bin SP not allowed for dept MDR
- MDR-0186.mdr ref=SP-C516: 8/9: bin SP not allowed for dept MDR
- MDR-0186.mdr ref=SP-C517: 8/9: bin SP not allowed for dept MDR
- MDR-0186.mdr ref=SP-C518: 8/9: bin SP not allowed for dept MDR
- MDR-0186.mdr ref=SP-C519: 8/9: bin SP not allowed for dept MDR
- MDR-0186.mdr ref=SP-C520: 8/9: bin SP not allowed for dept MDR
- MDR-0186.mdr ref=SP-C521: 8/9: bin SP not allowed for dept MDR
- MDR-0186.mdr ref=SP-C522: 8/9: bin SP not allowed for dept MDR
- MDR-0186.mdr ref=SP-C523: 8/9: bin SP not allowed for dept MDR
- MDR-0186.mdr ref=SP-C524: 8/9: bin SP not allowed for dept MDR
- MDR-0186.mdr ref=SP-C525: 8/9: bin SP not allowed for dept MDR
- MDR-0186.mdr ref=SP-C526: 8/9: bin SP not allowed for dept MDR
- MDR-0187.mdr ref=SP-C527: 8/9: bin SP not allowed for dept MDR
- MDR-0187.mdr ref=SP-C528: 8/9: bin SP not allowed for dept MDR
- MDR-0187.mdr ref=SP-C529: 8/9: bin SP not allowed for dept MDR
- MDR-0187.mdr ref=SP-C530: 8/9: bin SP not allowed for dept MDR
- MDR-0187.mdr ref=SP-C531: 8/9: bin SP not allowed for dept MDR
- MDR-0188.mdr (session): 7: Nora.K terminated after 2025-11-15
- MDR-0189.mdr (session): 12: weekend timestamp: 2025-11-01 10:57:00
- MDR-0190.mdr (session): P2: invalid processor: 'Webb.T'
- MDR-0191.mdr ref=SP-C574: 8/9: bin SP not allowed for dept MDR
- MDR-0191.mdr ref=SP-C575: 8/9: bin SP not allowed for dept MDR
- MDR-0191.mdr ref=SP-C576: 8/9: bin SP not allowed for dept MDR
- MDR-0191.mdr ref=SP-C577: 8/9: bin SP not allowed for dept MDR
- MDR-0191.mdr ref=SP-C578: 8/9: bin SP not allowed for dept MDR
- MDR-0191.mdr ref=SP-C579: 8/9: bin SP not allowed for dept MDR
- MDR-0191.mdr ref=SP-C580: 8/9: bin SP not allowed for dept MDR
- MDR-0191.mdr ref=SP-C581: 8/9: bin SP not allowed for dept MDR
- MDR-0191.mdr ref=SP-C582: 8/9: bin SP not allowed for dept MDR
- MDR-0191.mdr ref=SP-C583: 8/9: bin SP not allowed for dept MDR
- MDR-0191.mdr ref=SP-C584: 8/9: bin SP not allowed for dept MDR
- MDR-0191.mdr ref=SP-C585: 8/9: bin SP not allowed for dept MDR
- MDR-0191.mdr ref=SP-C586: 8/9: bin SP not allowed for dept MDR
- MDR-0191.mdr ref=SP-C587: 8/9: bin SP not allowed for dept MDR
- MDR-0191.mdr ref=SP-C588: 8/9: bin SP not allowed for dept MDR
- MDR-0192.mdr (session): 7: Nora.K terminated after 2025-11-15
- MDR-0193.mdr (session): P2: invalid processor: 'Harmon.D'
- MDR-0194.mdr (session): P2: invalid processor: 'Harmon.D'
- MDR-0195.mdr (session): 12: weekend timestamp: 2025-11-22 08:58:00
- MDR-0196.mdr ref=SP-C634: 8/9: bin SP not allowed for dept MDR
- MDR-0196.mdr ref=SP-C635: 8/9: bin SP not allowed for dept MDR
- MDR-0196.mdr ref=SP-C636: 8/9: bin SP not allowed for dept MDR
- MDR-0196.mdr ref=SP-C637: 8/9: bin SP not allowed for dept MDR
- MDR-0196.mdr ref=SP-C638: 8/9: bin SP not allowed for dept MDR
- MDR-0196.mdr ref=SP-C639: 8/9: bin SP not allowed for dept MDR
- MDR-0196.mdr ref=SP-C640: 8/9: bin SP not allowed for dept MDR
- MDR-0196.mdr ref=SP-C641: 8/9: bin SP not allowed for dept MDR
- MDR-0196.mdr ref=SP-C642: 8/9: bin SP not allowed for dept MDR
- MDR-0196.mdr ref=SP-C643: 8/9: bin SP not allowed for dept MDR
- MDR-0196.mdr ref=SP-C644: 8/9: bin SP not allowed for dept MDR
- MDR-0196.mdr ref=SP-C645: 8/9: bin SP not allowed for dept MDR
- MDR-0197.mdr ref=SP-C646: 8/9: bin SP not allowed for dept MDR
- MDR-0197.mdr ref=SP-C647: 8/9: bin SP not allowed for dept MDR
- MDR-0197.mdr ref=SP-C648: 8/9: bin SP not allowed for dept MDR
- MDR-0197.mdr ref=SP-C649: 8/9: bin SP not allowed for dept MDR
- MDR-0197.mdr ref=SP-C650: 8/9: bin SP not allowed for dept MDR
- MDR-0198.mdr (session): 12: weekend timestamp: 2025-10-26 08:47:00
- MDR-0199.mdr (session): 12: weekend timestamp: 2025-10-18 08:38:00
- MDR-0200.mdr (session): P6: timestamp outside Q4 2025: 2025-09-01 10:00:00
- MDR-0201.mdr (session): P2: invalid processor: 'Cross.R'
- MDR-0202.mdr ref=SP-C695: 8/9: bin SP not allowed for dept MDR
- MDR-0202.mdr ref=SP-C696: 8/9: bin SP not allowed for dept MDR
- MDR-0202.mdr ref=SP-C697: 8/9: bin SP not allowed for dept MDR
- MDR-0202.mdr ref=SP-C698: 8/9: bin SP not allowed for dept MDR
- MDR-0202.mdr ref=SP-C699: 8/9: bin SP not allowed for dept MDR
- MDR-0202.mdr ref=SP-C700: 8/9: bin SP not allowed for dept MDR
- MDR-0202.mdr ref=SP-C701: 8/9: bin SP not allowed for dept MDR
- MDR-0202.mdr ref=SP-C702: 8/9: bin SP not allowed for dept MDR
- MDR-0202.mdr ref=SP-C703: 8/9: bin SP not allowed for dept MDR
- MDR-0202.mdr ref=SP-C704: 8/9: bin SP not allowed for dept MDR
- MDR-0202.mdr ref=SP-C705: 8/9: bin SP not allowed for dept MDR
- MDR-0202.mdr ref=SP-C706: 8/9: bin SP not allowed for dept MDR
- MDR-0202.mdr ref=SP-C707: 8/9: bin SP not allowed for dept MDR
- MDR-0202.mdr ref=SP-C708: 8/9: bin SP not allowed for dept MDR
- MDR-0202.mdr ref=SP-C709: 8/9: bin SP not allowed for dept MDR
- MDR-0202.mdr ref=SP-C710: 8/9: bin SP not allowed for dept MDR
- MDR-0202.mdr ref=SP-C711: 8/9: bin SP not allowed for dept MDR
- MDR-0202.mdr ref=SP-C712: 8/9: bin SP not allowed for dept MDR
- MDR-0202.mdr ref=SP-C713: 8/9: bin SP not allowed for dept MDR
- MDR-0202.mdr ref=SP-C714: 8/9: bin SP not allowed for dept MDR
- MDR-0203.mdr ref=SP-C715: 8/9: bin SP not allowed for dept MDR
- MDR-0203.mdr ref=SP-C716: 8/9: bin SP not allowed for dept MDR
- MDR-0203.mdr ref=SP-C717: 8/9: bin SP not allowed for dept MDR
- MDR-0203.mdr ref=SP-C718: 8/9: bin SP not allowed for dept MDR
- MDR-0203.mdr ref=SP-C719: 8/9: bin SP not allowed for dept MDR
- MDR-0204.mdr (session): P6: timestamp outside Q4 2025: 2026-01-09 17:00:00
- MDR-0205.mdr (session): P2: invalid processor: 'Cross.R'
- MDR-0206.mdr (session): 7: Nora.K terminated after 2025-11-15
- MDR-0208.mdr (session): P1: invalid department: 'QA'
- MDR-0210.mdr (session): 7: Nora.K terminated after 2025-11-15
- MDR-0211.mdr (session): P2: invalid processor: 'Harmon.D'
- MDR-0212.mdr (session): P1: invalid department: 'QA'
- MDR-0213.mdr (session): P2: invalid processor: 'Cross.R'
- MDR-0214.mdr ref=PH-C846: P3: invalid bin: 'PH'
- MDR-0214.mdr ref=GR-C848: 10: value >= 1000.0: 4548.78
- MDR-0214.mdr ref=GR-C849: non-numeric value
- MDR-0214.mdr ref=GR-C851: P5: invalid value: -478.09
- MDR-0214.mdr ref=AX-C852: non-numeric value
- MDR-0214.mdr ref=AX-C854: P5: invalid value: -416.53
- MDR-0214.mdr ref=BL-C855: P4: invalid category: 'sigma'
- MDR-0214.mdr ref=BL-C857: non-numeric value
- MDR-0215.mdr ref=ZZ-C862: P3: invalid bin: 'ZZ'
- MDR-0215.mdr ref=BL-C867: non-numeric value
- MDR-0215.mdr ref=ZZ-C869: P3: invalid bin: 'ZZ'
- MDR-0216.mdr ref=GR-C877: P4: invalid category: 'omega'
- MDR-0216.mdr ref=GR-C878: P5: invalid value: -449.88
- MDR-0216.mdr ref=XX-C883: P3: invalid bin: 'XX'
- MDR-0216.mdr ref=GR-C887: P4: invalid category: 'omega'
- MDR-0217.mdr ref=BL-C889: P5: invalid value: -387.06
- MDR-0217.mdr ref=BL-C894: non-numeric value
- MDR-0217.mdr ref=PH-C897: P3: invalid bin: 'PH'
- MDR-0218.mdr ref=GR-C901: P4: invalid category: 'epsilon'
- MDR-0219.mdr ref=GR-C911: P4: invalid category: 'sigma'
- MDR-0219.mdr ref=GR-C915: P4: invalid category: 'zeta'
- MDR-0219.mdr ref=BL-C916: P4: invalid category: 'zeta'
- MDR-0220.mdr ref=AX-C918: P4: invalid category: 'zeta'
- MDR-0220.mdr ref=BL-C927: non-numeric value
- MDR-0220.mdr ref=GR-C932: 10: value >= 1000.0: 4922.17
- MDR-0221.mdr ref=AX-C937: P4: invalid category: 'sigma'
- MDR-0221.mdr ref=AX-C942: non-numeric value
- MDR-0221.mdr ref=XX-C944: P3: invalid bin: 'XX'
- MDR-0221.mdr ref=AX-C946: 10: value >= 1000.0: 1284.54
- MDR-0221.mdr ref=ZZ-C954: P3: invalid bin: 'ZZ'
- MDR-0221.mdr ref=AX-C956: P4: invalid category: 'sigma'
- MDR-0222.mdr ref=GR-C960: P5: invalid value: -227.46
- MDR-0222.mdr ref=GR-C964: P4: invalid category: 'epsilon'
- MDR-0222.mdr ref=GR-C965: P4: invalid category: 'zeta'
- MDR-0222.mdr ref=BL-C966: P5: invalid value: -407.96
- MDR-0222.mdr ref=BL-C967: P5: invalid value: -417.74
- MDR-0223.mdr ref=GR-C971: 10: value >= 1000.0: 4735.28
- MDR-0223.mdr ref=NV-C974: P3: invalid bin: 'NV'
- MDR-0224.mdr ref=GR-C992: 10: value >= 1000.0: 4518.43
- MDR-0224.mdr ref=AX-C993: P5: invalid value: -483.66
- MDR-0225.mdr ref=AX-C994: P4: invalid category: 'zeta'
- MDR-0225.mdr ref=GR-C995: P5: invalid value: -435.57
- MDR-0225.mdr ref=GR-D003: non-numeric value
- MDR-0225.mdr ref=BL-D005: P4: invalid category: 'zeta'
- MDR-0225.mdr ref=GR-D008: non-numeric value
- MDR-0226.mdr ref=BL-D014: 10: value >= 1000.0: 1633.55
- MDR-0226.mdr ref=GR-D017: 10: value >= 1000.0: 2310.16
- MDR-0226.mdr ref=BL-D018: P4: invalid category: 'omega'
- MDR-0226.mdr ref=AX-D019: non-numeric value
- MDR-0226.mdr ref=BL-D021: 10: value >= 1000.0: 1662.61
- MDR-0226.mdr ref=BL-D022: P5: invalid value: -201.84
- MDR-0226.mdr ref=AX-D023: 10: value >= 1000.0: 2717.25
- MDR-0226.mdr ref=BL-D029: 10: value >= 1000.0: 1489.21
- MDR-0227.mdr ref=AX-D032: 10: value >= 1000.0: 3295.79
- MDR-0227.mdr ref=NV-D038: P3: invalid bin: 'NV'
- MDR-0227.mdr ref=GR-D039: P5: invalid value: -331.31
- MDR-0227.mdr ref=GR-D040: P5: invalid value: -138.38
- MDR-0227.mdr ref=BL-D041: 10: value >= 1000.0: 2975.27
- MDR-0228.mdr ref=NV-D044: P3: invalid bin: 'NV'
- MDR-0228.mdr ref=XX-D046: P3: invalid bin: 'XX'
- MDR-0228.mdr ref=GR-D048: 10: value >= 1000.0: 2079.65
- MDR-0228.mdr ref=AX-D049: P4: invalid category: 'epsilon'
- MDR-0228.mdr ref=GR-D053: P5: invalid value: -144.32
- MDR-0228.mdr ref=BL-D056: P4: invalid category: 'zeta'
- MDR-0228.mdr ref=AX-D057: P4: invalid category: 'epsilon'
- MDR-0229.mdr ref=BL-D060: 10: value >= 1000.0: 4805.98
- MDR-0229.mdr ref=PH-D064: P3: invalid bin: 'PH'
- MDR-0229.mdr ref=GR-D065: non-numeric value
- MDR-0229.mdr ref=AX-D073: non-numeric value
- MDR-0230.mdr ref=BL-D074: P4: invalid category: 'omega'
- MDR-0230.mdr ref=AX-D075: non-numeric value
- MDR-0230.mdr ref=ZZ-D077: P3: invalid bin: 'ZZ'
- MDR-0230.mdr ref=GR-D079: 10: value >= 1000.0: 3376.02
- MDR-0230.mdr ref=AX-D087: non-numeric value
- MDR-0231.mdr ref=BL-D091: 10: value >= 1000.0: 4781.07
- MDR-0231.mdr ref=GR-D092: P4: invalid category: 'omega'
- MDR-0231.mdr ref=NV-D095: P3: invalid bin: 'NV'
- MDR-0231.mdr ref=GR-D097: 10: value >= 1000.0: 2815.43
- MDR-0231.mdr ref=GR-D098: non-numeric value
- MDR-0231.mdr ref=BL-D100: 10: value >= 1000.0: 4814.74
- MDR-0231.mdr ref=AX-D107: P5: invalid value: -457.2
- MDR-0232.mdr ref=AX-D112: P4: invalid category: 'epsilon'
- MDR-0232.mdr ref=AX-D113: non-numeric value
- MDR-0232.mdr ref=XX-D115: P3: invalid bin: 'XX'
- MDR-0232.mdr ref=AX-D116: 10: value >= 1000.0: 4287.76
- MDR-0232.mdr ref=AX-D118: non-numeric value
- MDR-0232.mdr ref=BL-D120: P4: invalid category: 'zeta'
- MDR-0232.mdr ref=XX-D123: P3: invalid bin: 'XX'
- MDR-0233.mdr ref=GR-D128: non-numeric value
- MDR-0233.mdr ref=BL-D133: non-numeric value
- MDR-0233.mdr ref=BL-D136: non-numeric value
- MDR-0234.mdr ref=AX-D140: 10: value >= 1000.0: 3337.97
- MDR-0234.mdr ref=PH-D143: P3: invalid bin: 'PH'
- MDR-0235.mdr ref=BL-D150: 10: value >= 1000.0: 1901.99
- MDR-0235.mdr ref=ZZ-D153: P3: invalid bin: 'ZZ'
- MDR-0235.mdr ref=GR-D154: P4: invalid category: 'omega'
- MDR-0235.mdr ref=BL-D155: non-numeric value
- MDR-0235.mdr ref=GR-D159: P5: invalid value: -488.73
- MDR-0235.mdr ref=GR-D166: 10: value >= 1000.0: 1557.15
- MDR-0236.mdr ref=PH-D168: P3: invalid bin: 'PH'
- MDR-0236.mdr ref=NV-D174: P3: invalid bin: 'NV'
- MDR-0236.mdr ref=AX-D176: P5: invalid value: -225.23
- MDR-0237.mdr ref=GR-D177: P5: invalid value: -205.7
- MDR-0237.mdr ref=AX-D178: non-numeric value
- MDR-0237.mdr ref=PH-D181: P3: invalid bin: 'PH'
- MDR-0237.mdr ref=BL-D182: P5: invalid value: -461.81
- MDR-0237.mdr ref=AX-D187: P5: invalid value: -360.11
- MDR-0237.mdr ref=AX-D188: P4: invalid category: 'omega'
- MDR-0238.mdr ref=BL-D191: P5: invalid value: -470.14
- MDR-0238.mdr ref=AX-D194: P5: invalid value: -484.35
- MDR-0238.mdr ref=BL-D201: P5: invalid value: -434.06
- MDR-0238.mdr ref=GR-D202: 10: value >= 1000.0: 2350.13
- MDR-0239.mdr ref=AX-D203: 10: value >= 1000.0: 1497.23
- MDR-0239.mdr ref=BL-D206: 10: value >= 1000.0: 2634.44
- MDR-0239.mdr ref=GR-D209: P5: invalid value: -426.55
- MDR-0239.mdr ref=BL-D211: non-numeric value
- MDR-0239.mdr ref=BL-D212: 10: value >= 1000.0: 3161.77
- MDR-0239.mdr ref=BL-D213: P4: invalid category: 'omega'
- MDR-0240.mdr ref=BL-D219: P4: invalid category: 'sigma'
- MDR-0240.mdr ref=AX-D225: P4: invalid category: 'epsilon'
- MDR-0240.mdr ref=GR-D226: 10: value >= 1000.0: 3772.29
- MDR-0241.mdr ref=XX-D235: P3: invalid bin: 'XX'
- MDR-0241.mdr ref=XX-D237: P3: invalid bin: 'XX'
- MDR-0241.mdr ref=BL-D238: non-numeric value
- MDR-0241.mdr ref=AX-D240: 10: value >= 1000.0: 4976.54
- MDR-0241.mdr ref=BL-D241: 10: value >= 1000.0: 3962.79
- MDR-0241.mdr ref=NV-D245: P3: invalid bin: 'NV'
- MDR-0241.mdr ref=AX-D246: P4: invalid category: 'omega'
- MDR-0241.mdr ref=BL-D247: P5: invalid value: -357.37
- MDR-0241.mdr ref=GR-D251: 10: value >= 1000.0: 2946.54
- MDR-0241.mdr ref=BL-D252: P4: invalid category: 'omega'
- MDR-0242.mdr ref=NV-D256: P3: invalid bin: 'NV'
- MDR-0242.mdr ref=BL-D262: 10: value >= 1000.0: 3827.24
- MDR-0243.mdr ref=AX-D267: P4: invalid category: 'omega'
- MDR-0243.mdr ref=GR-D274: P4: invalid category: 'zeta'
- MDR-0243.mdr ref=BL-D276: P5: invalid value: -151.52
- MDR-0243.mdr ref=BL-D279: P4: invalid category: 'epsilon'
- MDR-0244.mdr ref=GR-D282: P5: invalid value: -232.0
- MDR-0244.mdr ref=GR-D284: non-numeric value
- MDR-0244.mdr ref=BL-D285: 10: value >= 1000.0: 3619.73
- MDR-0244.mdr ref=BL-D288: P4: invalid category: 'sigma'
- MDR-0245.mdr ref=GR-D290: 10: value >= 1000.0: 1135.11
- MDR-0245.mdr ref=GR-D293: P5: invalid value: -452.22
- MDR-0245.mdr ref=GR-D296: P5: invalid value: -311.71
- MDR-0246.mdr ref=GR-D303: P4: invalid category: 'sigma'
- MDR-0246.mdr ref=AX-D304: P5: invalid value: -470.53
- MDR-0246.mdr ref=AX-D309: P5: invalid value: -39.39
- MDR-0246.mdr ref=XX-D312: P3: invalid bin: 'XX'
- MDR-0246.mdr ref=BL-D314: non-numeric value
- MDR-0247.mdr ref=AX-D316: non-numeric value
- MDR-0247.mdr ref=GR-D318: P5: invalid value: -424.83
- MDR-0247.mdr ref=XX-D320: P3: invalid bin: 'XX'
- MDR-0247.mdr ref=PH-D324: P3: invalid bin: 'PH'
- MDR-0247.mdr ref=GR-D326: P4: invalid category: 'sigma'
- MDR-0247.mdr ref=PH-D328: P3: invalid bin: 'PH'
- MDR-0248.mdr ref=GR-D330: non-numeric value
- MDR-0248.mdr ref=NV-D332: P3: invalid bin: 'NV'
- MDR-0248.mdr ref=BL-D334: P5: invalid value: -322.51
- MDR-0248.mdr ref=BL-D339: 10: value >= 1000.0: 3913.97
- MDR-0248.mdr ref=GR-D340: non-numeric value
- MDR-0248.mdr ref=AX-D341: 10: value >= 1000.0: 2313.81
- MDR-0249.mdr ref=AX-D342: 10: value >= 1000.0: 4982.95
- MDR-0249.mdr ref=ZZ-D347: P3: invalid bin: 'ZZ'
- MDR-0249.mdr ref=ZZ-D350: P3: invalid bin: 'ZZ'
- MDR-0249.mdr ref=GR-D354: non-numeric value
- MDR-0249.mdr ref=XX-D357: P3: invalid bin: 'XX'
- MDR-0249.mdr ref=AX-D358: non-numeric value
- MDR-0249.mdr ref=PH-D360: P3: invalid bin: 'PH'
- MDR-0249.mdr ref=BL-D362: 10: value >= 1000.0: 2231.13
- MDR-0250.mdr ref=GR-D363: 10: value >= 1000.0: 1903.84
- MDR-0250.mdr ref=GR-D364: P4: invalid category: 'zeta'
- MDR-0250.mdr ref=BL-D365: P5: invalid value: -113.82
- MDR-0250.mdr ref=BL-D367: non-numeric value
- MDR-0250.mdr ref=GR-D368: 10: value >= 1000.0: 1363.03
- MDR-0250.mdr ref=NV-D371: P3: invalid bin: 'NV'
- MDR-0250.mdr ref=BL-D372: non-numeric value
- MDR-0250.mdr ref=ZZ-D374: P3: invalid bin: 'ZZ'
- MDR-0250.mdr ref=BL-D376: 10: value >= 1000.0: 4008.18
- MDR-0250.mdr ref=AX-D380: P4: invalid category: 'epsilon'
- SA-0067.csv (session): 7: Nora.K terminated after 2025-11-15
- SA-0069.csv ref=SP-E235: 8/9: bin SP not allowed for dept MDR
- SA-0069.csv ref=SP-E236: 8/9: bin SP not allowed for dept MDR
- SA-0069.csv ref=SP-E237: 8/9: bin SP not allowed for dept MDR
- SA-0069.csv ref=SP-E238: 8/9: bin SP not allowed for dept MDR
- SA-0069.csv ref=SP-E239: 8/9: bin SP not allowed for dept MDR
- SA-0069.csv ref=SP-E240: 8/9: bin SP not allowed for dept MDR
- SA-0069.csv ref=SP-E241: 8/9: bin SP not allowed for dept MDR
- SA-0069.csv ref=SP-E242: 8/9: bin SP not allowed for dept MDR
- SA-0072.csv (session): P1: invalid department: 'TESTING'
- SA-0077.csv (session): 7: Nora.K terminated after 2025-11-15
- SA-0078.csv (session): P1: invalid department: 'TESTING'
- SA-0080.csv (session): P1: invalid department: 'HR'
- SA-0081.csv (session): 7: Nora.K terminated after 2025-11-15
- SA-0083.csv (session): P1: invalid department: 'QA'
- SA-0084.csv (session): 7: Nora.K terminated after 2025-11-15
- SA-0085.csv (session): P1: invalid department: 'HR'
- WB-0036.txt (session): P1: invalid department: 'MR'
- WB-0037.txt ref=SP-F076: 8/9: bin SP not allowed for dept MDR
- WB-0037.txt ref=SP-F077: 8/9: bin SP not allowed for dept MDR
- WB-0037.txt ref=SP-F078: 8/9: bin SP not allowed for dept MDR
- WB-0037.txt ref=SP-F079: 8/9: bin SP not allowed for dept MDR
- WB-0037.txt ref=SP-F080: 8/9: bin SP not allowed for dept MDR
- WB-0037.txt ref=SP-F081: 8/9: bin SP not allowed for dept MDR
- WB-0037.txt ref=SP-F082: 8/9: bin SP not allowed for dept MDR
- WB-0037.txt ref=SP-F083: 8/9: bin SP not allowed for dept MDR
- WB-0037.txt ref=SP-F084: 8/9: bin SP not allowed for dept MDR
- WB-0037.txt ref=SP-F085: 8/9: bin SP not allowed for dept MDR
- WB-0037.txt ref=SP-F086: 8/9: bin SP not allowed for dept MDR
- WB-0037.txt ref=SP-F087: 8/9: bin SP not allowed for dept MDR
- WB-0037.txt ref=SP-F088: 8/9: bin SP not allowed for dept MDR
- WB-0037.txt ref=SP-F089: 8/9: bin SP not allowed for dept MDR
- WB-0041.txt (session): P1: invalid department: 'TESTING'
- WB-0043.txt (session): 7: Nora.K terminated after 2025-11-15








# Some more detailed writting in case of curiosity

## The portal

The PDF welcome packet has a QR code poiting at `https://d1ihdmbljgo2cz.cloudfront.net`. The portal lays out the standard validation framework. Six rules every quarterly entry has to satisfy:

1. **Department** must be one of `MDR`, `SA`, `WB`.
2. **Processor** must be one of the seven listed in the directory.
3. **Bin** must be one of the four signals: `GR`, `BL`, `AX`, `SP`.
4. **Category** must be `alpha`, `beta`, `gamma`, or `delta`. Case-sensitive.
5. **Value** must be a positive number.
6. **Timestamp** must fall within Q4 2025 (Oct 1 to Dec 31).

The portal also references a Compliance Annex at `compliance.html`, behind a "facility access code" form.

## The gate

I clicked the submit button with devtools open. No network request fired, so I conclude the check runs in the browser, I qucikly located the JS associated with the event:

```js
var H = "38b19f2e76c9fa1e3ab74c80fb3e95b3cd761ce39b0e2359b6ac15e012220907";
var SUFFIX = "arturic";

// 1. SHA-256(input.trim().toUpperCase()) must equal H
// 2. Redirect to SHA-256(input + "arturic") + ".html"
```

Two things follow from this. The validator is fully available offline, so we can just brute force, if the password simple enough.

## Aside: the clue I tried first

To be honest, I first tried using the hint on `compliance.html`:

> Your facility access code corresponds to your assigned location. Consult your facility photograph for orientation.

Doing a google image search on `facility_exterior.png` I arrived at  Bell Labs Holmdel Complex.

I tried some strings against the hash. `HOLMDEL`, `BELLWORKS`, `BELL LABS`, `EAST ENTRANCE`, `LUMON`, `ARTURIC`, the ZIP code, address fragments, room codes from `layout.html`. Nothing matched.

Then I've tried brute force.
It quickly returned `JANSKY`, it does make sense: Karl Guthe Jansky worked at Bell Labs Holmdel and in 1932 picked up radio waves coming from the Milky Way, founding radio astronomy, I didn't know him before hand.

## Brute force

Input is uppercased and trimmed, so the charset is `[A-Z0-9]`.
Code in [`crack.py`](./crack.py). A `multiprocessing.Pool` splits the space by first byte (36 tasks) and walks the rest with `itertools.product`. It increments length from 1 until it hits.

It hit at length 6, around 13 seconds in:

```
*** MATCH (len=6): 'JANSKY' ***
Hidden URL: 4444047137b637db776afcf437a789d36820221ca5cf3039762b1c6af4e3b867.html
```

## The hidden compliance annex

That URL serves a page with six more rules:

1. **Terminated processor.** Entries from `Nora.K` after 2025-11-15 are invalid.
2. **SP bin restricted to SA.** Any other department using `SP` is non-compliant.
3. **Department to bin matrix.** `MDR={GR,BL,AX}`, `SA={SP,BL}`, `WB={GR,AX}`. Cross-department assignments are invalid.
4. **Value cap.** Values at or above 1000.00 are flagged.
5. **Unique session IDs.** Duplicates collapse to the entry with the earliest timestamp.
6. **Weekdays only.** Saturday and Sunday sessions are out.

These apply retroactively to all Q4 2025 data, alongside the public six.

## Processing, all rules enforced

`main.py` parses each session into `Session` and `Entry` dataclasses, then applies all twelve rules.

Public (from `manual.html`):

1. `department ∈ {MDR, SA, WB}`, in `validate_session`
2. `processor ∈ directory`, in `validate_session`
3. `bin ∈ {GR, BL, AX, SP}`, in `validate_entry`
4. `category ∈ {alpha, beta, gamma, delta}`, case-sensitive, in `validate_entry`
5. `value > 0`, in `validate_entry`
6. `Q4_START <= timestamp <= Q4_END`, in `validate_session`

Hidden (from the compliance annex):

7. `processor == "Nora.K" and timestamp.date() > 2025-11-15` is invalid, in `validate_session`
8/9. `bin ∈ DEPT_BIN_MATRIX[department]` and `bin == "SP"` only when `department == "SA"`, in `validate_entry`
10. `value < 1000.00`, in `validate_entry`
11. Unique `session_id`, in `dedupe_sessions`, keeping the earliest timestamp
12. `timestamp.weekday() < 5`, Mon to Fri, in `validate_session`

If `validate_session` flags a session, all its entries are dropped. Otherwise each entry is checked on its own with `validate_entry`, and only the fully valid ones make it into the total.

## The result

```bash
uv run python main.py
```

```
Sessões consideradas (após dedupe): 400
Anomalias encontradas: 521
...
Soma total de entradas válidas: 1023118.20
```
