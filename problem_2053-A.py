#Tender Carpenter

def calc(t, test_cases):
    for n, a in test_cases:
        for x in range(n):
            

t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))

results = calc(t, test_cases)

for res in results:
    print(res)
