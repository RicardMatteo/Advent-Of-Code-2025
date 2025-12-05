ranges_text, ids = open("Day05/input").read().split("\n\n")
ranges = sorted([tuple(map(int, r.split("-"))) for r in ranges_text.splitlines()])
merged = [ranges.pop(0)]
for s, e in ranges:
    if merged[-1][1] >= s - 1:
        merged[-1] = (merged[-1][0], max(merged[-1][1], e))
    else:
        merged.append((s, e))

print(sum(any(s <= int(id) <= e for s, e in merged) for id in ids.splitlines()))
print(sum(e - s + 1 for s, e in merged))