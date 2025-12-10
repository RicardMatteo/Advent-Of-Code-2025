import re
from z3 import Optimize, Int, Sum, sat

def solve(targets, buttons, is_part1):
    opt = Optimize()
    x = [Int(f'x{i}') for i in range(len(buttons))]

    opt.add([v >= 0 for v in x])
    if is_part1: 
        opt.add([v <= 1 for v in x])

    for i, val in enumerate(targets):
        btn_sum = Sum([x[j] for j, btn in enumerate(buttons) if i in btn])
        opt.add(btn_sum % 2 == val if is_part1 else btn_sum == val)
    
    opt.minimize(Sum(x))
    return opt.model().eval(Sum(x)).as_long() if opt.check() == sat else 0

p1, p2 = 0, 0

for line in filter(None, open("Day10/input").read().splitlines()):
    lights = [1 if c == '#' else 0 for c in re.search(r'\[(.*?)\]', line).group(1)]
    btns   = [[int(k) for k in b.split(',')] if b else [] for b in re.findall(r'\((.*?)\)', line)]
    jolts  = [int(n) for n in re.search(r'\{(.*?)\}', line).group(1).split(',')]

    p1 += solve(lights, btns, True)
    p2 += solve(jolts, btns, False)

print(f"Part 1: {p1}\nPart 2: {p2}")