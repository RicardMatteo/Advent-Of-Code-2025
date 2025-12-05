p1 = p2 = 0
cur = 50
for l in open("Day01/input", "r").read().splitlines():
    v = int(l[1:]) * (1 if l[0] == "R" else -1)
    p1 += cur == 0
    p2 += abs((v + cur) // 100) - (v < 0 and cur == 0) + (v < 0 and (cur + v) % 100 == 0)
    cur = (cur + v) % 100
print(p1, p2)