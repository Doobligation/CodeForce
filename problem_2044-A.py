#Easy Problem

def calc(t, test_cases):
    results = []

    for n in test_cases:
        results.append(n-1)

    return results

t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    test_cases.append(n)

results = calc(t, test_cases)

for res in results:
    print(res)
