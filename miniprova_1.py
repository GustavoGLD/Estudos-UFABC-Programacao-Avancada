"""
[1, 2, 0]
[3, 1, 2]
[4, 3, 1]
[7, 4, 3]
[11, 7, 4]

[n, np, npp]
[n+np, n, np]

n -> n+np
np -> n
npp -> np
"""

n, np, npp = 1, 2, 0

for _ in range(int(input())):
    npp = np
    np = n
    n = np + npp
    print(n, np, npp)

print(n)
