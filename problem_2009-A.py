# Minimize!
# import math

def calc(t, test_cases):
    results = []

    for case in test_cases:
        a = case[0]
        b = case[1]
        # avg = int((a + b) / 2)
        # res = a
        results.append(b - a)

    return results
            


t = int(input())
test_cases = []

for _ in range(t):
    a, b = map(int, input().split())
    test_cases.append([a, b])

results = calc(t, test_cases)

for res in results:
    print(res)