from itertools import accumulate

p1 = p2 = 0
input = open("template2/inputtest", "r").read().splitlines()
for i in range(len(input)-1):
    line = input[i].strip().split()
    line = [int(x) for x in line]
    input[i] = line

# put the column symbols in a list
    
    
symbols = input[-1].strip().split()
colomn = []
for i in range(len(symbols)):
    colomn.append([str(x[i]) for x in input[:-1]])

print(colomn)


# ['64', '23', '314'] -> [623, 431, 4]
def rotate_colomn(lst):
    l = max(len(x) for x in lst)
    vals = [""] * l
    for x in lst:
        for i in range(len(x), 0, -1):
            vals[l-i] = x[i-1] + vals[l-i]
    return vals
rotated_colomn = rotate_colomn(colomn)
print(rotated_colomn)




for j in range(len(symbols)):
    if symbols[j] == '+':
        p1 += sum(int(input[i][j]) for i in range(len(input)-1))
    elif symbols[j] == '*':
        prod = 1
        for i in range(len(input)-1):
            prod *= int(input[i][j])
        p1 += prod



print(p1, p2)
