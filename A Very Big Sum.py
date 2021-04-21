n = int(input())
ar = list(map(int, input().rstrip().split()))
def aVeryBigSum(ar):
    res = 0
    for i in ar:
        res +=i
    return res
result = aVeryBigSum(ar)
print(result)
