# Normal Problem

def calc(t, test_cases):
    results = []

    for n in test_cases:
        transformed = []
        for x in range(len(n)):
            if n[x] == 'p':
                transformed = ['q'] + transformed
            elif n[x] == 'q':
                transformed = ['p'] + transformed

            else:
                transformed = ['w'] + transformed
    
        results.append(''.join(transformed))

    return results
            

t = int(input())
test_cases = []

for _ in range(t):
    a = list(str(input()))
    test_cases.append(a)

results = calc(t, test_cases)

for res in results:
    print(res)
