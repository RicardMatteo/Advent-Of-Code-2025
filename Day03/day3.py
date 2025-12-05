def pick_max_digits(s, k):
    i, out = 0, []
    for r in range(k, 0, -1):
        mi, m = max(enumerate(s[i:len(s) - r + 1]), key=lambda item: item[1])
        i += mi + 1
        out.append(m)
    return int(''.join(out))

lines = open("Day03/input", "r").read().splitlines()
print("p1 : ", sum(pick_max_digits(l,  2) for l in lines))
print("p2 : ", sum(pick_max_digits(l, 12) for l in lines))