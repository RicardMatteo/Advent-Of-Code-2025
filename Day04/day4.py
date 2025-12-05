input = open("Day04/input", "r").read().splitlines()

coords = {(r, c): ch == '@' for r, line in enumerate(input) for c, ch in enumerate(line)}
stack = [(x, y) for x, l in enumerate(input) for y, _ in enumerate(l) if coords.get((x, y))]
dirs = ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))

p1 = sum(1 for x, y in stack if sum(coords.get((x + dx, y + dy), False) for dx, dy in dirs) < 4)
p2 = 0

while stack:
    x, y = stack.pop()
    if coords.get((x, y)) and sum(coords.get((x + dx, y + dy), False) for dx, dy in (dirs)) < 4:
        p2 += 1
        coords[(x, y)] = False
        stack.extend((x + dx, y + dy) for dx, dy in (dirs))

print(p1, p2)