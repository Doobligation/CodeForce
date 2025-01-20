# Turtle and Good Strings

def calc(t, test_cases):
    results = []
    
    for case in test_cases:
        n, a, b = case[0], case[1], case[2]

        pairs = n // 2
        remainder = n % 2

        cost_pairs = pairs * min(b, 2*a)
        cost_remainder = remainder * a
        
        results.append(cost_pairs + cost_remainder)
    
    return results


t= int(input())
test_cases = []

for _ in range(t):
    n, a, b = list(map(int, input().split()))
    test_cases.append([n, a, b])

results = calc(t, test_cases)

for res in results:
    print(res)

