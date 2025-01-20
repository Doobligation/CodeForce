# Fibonacciness
# import math

def calc(t, test_cases):
    results = []

    for case in test_cases:
        print(case)
    return results
            


t = int(input())
test_cases = []

for _ in range(t):
    temp = []

    n, k = map(int, input().split())
    temp.append([n,k])

    for x in range(n):
        inputs = list(map(int, input().split()))
        temp.append(inputs)
    
    test_cases.append(temp)

results = calc(t, test_cases)

for res in results:
    print(res)