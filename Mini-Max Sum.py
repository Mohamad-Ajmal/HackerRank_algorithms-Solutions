arr = list(map(int, input().rstrip().split()))
def miniMaxSum(arr):
    arr.sort()
    print(sum(arr[:-1]),sum(arr[1:]))
result = miniMaxSum(arr)
print(result)