# A+B Again?

def calc(t, test_cases):
    results = []
    for case in test_cases:
        results.append(int(case[0])+int(case[1]))
    
    return results

t = int(input())
test_cases = []

for _ in range(t):
    n = str(input())
    test_cases.append(n)

results = calc(t, test_cases)

for res in results:
    print(res)