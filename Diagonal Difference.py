n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
def diagonalDifference(arr):
    # Write your code here
    leftdiagonalsum,rightdiagonalsum = 0, 0
    arr_len = len(arr)
    i = 0
    j = 0
    while(i<arr_len):
        leftdiagonalsum += arr[i][j]
        i +=1
        j +=1
    i = 0
    j = arr_len-1
    while(i<arr_len):
        rightdiagonalsum +=arr[i][j]
        i +=1
        j -=1
    return abs(leftdiagonalsum - rightdiagonalsum)
    
result = diagonalDifference(arr)
print(result)