raw_data = open('Day12/inputtest').read().strip().split('\n\n')
shapes = {}
regions = []

for section in raw_data:
    lines = section.splitlines()
    header = lines[0]
    if 'x' in header:
        for line in lines:
            if not line.strip(): continue
            dim, counts = line.split(':')
            w, h = map(int, dim.split('x'))
            pieces = []
            for pid, count in enumerate(map(int, counts.split())):
                pieces.extend([pid] * count)
            regions.append((w, h, pieces))
    else:
        sid = int(header.replace(':', ''))
        coords = {(r, c) for r, l in enumerate(lines[1:]) for c, x in enumerate(l) if x == '#'}
        shapes[sid] = coords

def get_masks(w, h, shape_coords):
    masks = set()
    base = list(shape_coords)
    for _ in range(2):
        for _ in range(4):
            min_r, min_c = min(r for r, c in base), min(c for r, c in base)
            norm = [(r-min_r, c-min_c) for r, c in base]
            max_r, max_c = max(r for r, c in norm), max(c for r, c in norm)
            
            for r in range(h - max_r):
                for c in range(w - max_c):
                    m = 0
                    for dr, dc in norm:
                        m |= 1 << ((r+dr)*w + (c+dc))
                    masks.add(m)
            base = [(c, -r) for r, c in base]
        base = [(r, -c) for r, c in base]
    return sorted(list(masks), reverse=True)

def solve(w, h, p_ids):
    if sum(len(shapes[p]) for p in p_ids) > w * h: 
        return False
    
    pool = {pid: get_masks(w, h, shapes[pid]) for pid in set(p_ids)}
    queue = [(pid, pool[pid]) for pid in p_ids]
    queue.sort(key=lambda x: len(x[1]))

    def backtrack(idx, board):
        if idx == len(queue): return True
        _, valid_masks = queue[idx]
        for m in valid_masks:
            if not (board & m):
                if backtrack(idx + 1, board | m): 
                    return True
        return False

    return backtrack(0, 0)

total = 0
for i, (w, h, pieces) in enumerate(regions):
    print(f"Region {i+1} ({w}x{h}): ", end="", flush=True)
    if solve(w, h, pieces):
        print("OK")
        total += 1
    else:
        print("NOP")

print(f"Part 1 : {total}")