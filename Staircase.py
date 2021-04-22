n = int(input())
def staircase(n):
    for i in range(n):
        for j in range(1, n+1):
            if i + j >= n:
                print("#", end='')
            else:
                print(" ", end='')
        print()
result = staircase(n)
print(result)