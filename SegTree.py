import sys
inf = float('inf')
arrLen, conditions = map(int, sys.stdin.readline().rstrip().split())
val = 1
while val <= arrLen:
    val *= 2
arr = [inf]*val
for i in range(arrLen):
    arr.append(int(sys.stdin.readline().rstrip()))
    tempIndex = val+i
    while tempIndex > 1:
        tempIndex //= 2
        arr[tempIndex] = min(arr[tempIndex], arr[val+i])
for i2 in range(val-arrLen):
    arr.append(0)
# print(arr)


def f(cs, ce, s, e, ind):
    if s <= cs and ce <= e:
        return arr[ind]
    if ce < s or cs > e:
        return inf
    mid = (cs+ce)//2
    left = f(cs, mid, s, e, ind*2)
    right = f(mid + 1, ce, s, e, ind*2 + 1)
    return min(right, left)


for i in range(conditions):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(f(0, val - 1, a-1, b-1, 1))
