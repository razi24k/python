Dict = {"Sam": {"M1": 89, "M2": 56, "M3": 89},
        "Suresh": {"M1": 49, "M2": 96, "M3": 89}}

for key, value in Dict.items():
    print(key)
    for x, y in value:
        print(f"{x}: {y}")