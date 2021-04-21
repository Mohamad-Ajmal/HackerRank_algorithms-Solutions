a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))

def compareTriplets(a,b):
    answer = []
    alice, bob = 0, 0
    for alice_s, bob_s in zip(a, b):
        if alice_s > bob_s:
            alice += 1
        if alice_s < bob_s:
            bob += 1
    answer.append(alice)
    answer.append(bob)
    return answer
    
result = compareTriplets(a, b)
print(result)
