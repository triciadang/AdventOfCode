import re

with open("./input5.txt") as f:
    almanac = f.read().strip().split("\n\n")

seeds = [int(s) for s in re.findall(r"(\d+)", almanac[0])]
maps = []
for i in range(1, len(almanac)):
    txt = almanac[i].strip().split("\n")[1:]
    map = [[int(s) for s in re.findall(r"(\d+)", line)] for line in txt]
    map = [{"start": x, "end": x + r - 1, "add": y - x} for y, x, r in map]
    map = sorted(map, key=lambda f: f["start"])

    zero = [
        {"start": float("-inf"), "end": map[0]["start"] - 1, "add": 0},
        {"start": map[-1]["end"], "end": float("inf"), "add": 0},
    ]
    for i in range(1, len(map) - 1):
        end, start = map[i]["end"], map[i + 1]["start"]
        if start - end > 1:
            zero.append({"start": end + 1, "end": start - 1, "add": 0})
    map += zero

    maps.append(map)

batches = [
    {"start": seeds[i], "end": seeds[i] + seeds[i + 1]} for i in range(0, len(seeds), 2)
]

for map in maps:
    new_batches = []

    for batch in batches:
        funcs = [
            f for f in map if f["start"] <= batch["end"] and f["end"] >= batch["start"]
        ]

        for f in funcs:
            new_batches.append(
                {
                    "start": max(batch["start"], f["start"]) + f["add"],
                    "end": min(batch["end"], f["end"]) + f["add"],
                }
            )

    batches = new_batches

print(min(batch["start"] for batch in batches))