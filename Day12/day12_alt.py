sections = open('Day12/input').read().strip().split('\n\n')
sizes = {int(s.split(':')[0]): s.count('#') for s in sections if 'x' not in s.split('\n')[0]}
valid = 0

for section in sections:
    if 'x' in section.split('\n')[0]:
        for line in section.splitlines():
            if line:
                dim, counts = line.split(':')
                w, h = map(int, dim.split('x'))
                needed = sum(n * sizes[i] for i, n in enumerate(map(int, counts.split())))
                if needed <= w * h:
                    valid += 1

print(valid)