n = int(input().strip())
candles = list(map(int, input().rstrip().split()))
def birthdayCakeCandles(candles):
    return candles.count(max(candles))
result = birthdayCakeCandles(candles)
print(result)