 #problem 2051 - A

def calc(t, test_cases):
    results = []

    for n, a, b in test_cases:
        res = 0
        for i in range(n):
            if i == n-1:
                res += a[i]
                break
            if a[i] > b[i+1]:
                res += a[i] - b[i+1]
        
        results.append(res)
    
    return results

t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    test_cases.append((n, a, b))

results = calc(t, test_cases)

for res in results:
    print(res)
