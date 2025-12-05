ranges = [tuple(map(int, r.split("-"))) for r in open("Day02/input").read().split(",")]

def is_invalid(x, y=1):
    s = str(x)
    return any(s[:l] * (len(s) // l) == s for l in range(y , len(s) // 2 + 1))

p1 = sum(i for a, b in ranges for i in range(a, b + 1) if len(str(i)) % 2 == 0 and is_invalid(i,len(str(i)) // 2))
p2 = sum(i for a, b in ranges for i in range(a, b + 1) if is_invalid(i))
print(p1, p2)