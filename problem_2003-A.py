# Turtle and Good Strings

def calc(t, test_cases):
    results = []
    s = ""
    count = 0
    
    for case in test_cases:
        n = case[0]
        t_i = case[1]

        s += t_i

        if s[0] == s[n-1]:
            results.append("NO")
        else:
            results.append("YES")
        
        count += n

    
    return results


t= int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    s = str(input())
    test_cases.append((n, s))

results = calc(t, test_cases)

for res in results:
    print(res)

