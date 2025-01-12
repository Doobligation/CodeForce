# Hard Problem
def calc(t, test_cases):
    results = []

    for m, a, b, c in test_cases:
        res = 0

        if m <= a and m <= b:
            res = 2*m

        if m <= a and m > b:
            res += (m+b) + min(m - b, c)
            
        
        if m > a and m <= b:
            res += (m + a) + min(m- a, c)
        
        if m > a and m > b:
            res += (a + b) + min((2*m - a - b), c)
        
        results.append(res)

    return results

        

t = int(input())
test_cases = []

for _ in range(t):
    test_cases.append(tuple(map(int, input().split())))
    

results = calc(t, test_cases)

for res in results:
    print(res)