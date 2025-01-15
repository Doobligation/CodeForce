# Two Frogs

def calc(t, test_cases):
    results = []

    for n, a, b in test_cases:
        if (abs(a - b) % 2) == 1:
            results.append("NO")
        else:
            results.append("YES")

    return results


t = int(input())
test_cases = []
    
for _ in range(t):
    nani = tuple(map(int, input().split()))
    test_cases.append(nani)
    
results = calc(t, test_cases)

for res in results:
    print(res)