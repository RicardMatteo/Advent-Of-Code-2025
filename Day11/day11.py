from functools import cache

with open("Day11/input") as f:
    data = {k.strip(): v.split() for line in f for k, v in [line.split(":")]}

@cache
def dfs(node, fft=False, dac=False):
    if node == "out":
        return fft and dac
    return sum(dfs(nei, fft or nei == "fft", dac or nei == "dac") for nei in data[node])

print("Part 1:", dfs("you", True, True))
print("Part 2:", dfs("svr"))