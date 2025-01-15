# Crafting

def calc(t, test_cases):
    results = []

    for n, a, b in test_cases:
        if sum(a) < sum(b):
            results.append("NO")
            continue
        elif n == 2 and sum(a) >= sum(b):
            results.append("YES")
            continue
        elif sum(a) == sum(b):
            for x in range(n):
                if a[x] < b[x]:
                    results.append("NO")
                    break
                else:
                    results.append("YES")
                    break
        else:
            for x in range(n):
                if a[x] < b[x]:
                    a = [z - 1 for z in a]
                    a[x] += 2
                    negative_checker = any(z < 0 for z in a)

                    if negative_checker:
                        results.append("NO")
                        break
            if len(results) < len(test_cases):
                if sum(a) < sum(b):
                    results.append("NO")
                else:
                    results.append("YES")
                    

    return results


t = int(input())
test_cases = []
    
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    test_cases.append([n, a, b])
    
results = calc(t, test_cases)

for res in results:
    print(res)