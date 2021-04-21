n = int(input())
arr = list(map(int, input().rstrip().split()))
def plusMinus(arr):
    positive = sum(x > 0 for x in arr) / len(arr)
    negative = sum(x < 0 for x in arr) / len(arr)
    zero = sum(x == 0 for x in arr) / len(arr)
    print("{0:.6f}".format(positive))
    print("{0:.6f}".format(negative))
    print("{0:.6f}".format(zero))
res = plusMinus(arr)
print(res)

