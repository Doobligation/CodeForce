def calc(t, test_cases):
    results = []
    
    for n, arr in test_cases:
        freq = {}
        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
    
            score = 0
        for count in freq.values():
            score += count // 2
        
        results.append(score)
    
    return results

t = int(input())
test_cases = []
    
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    test_cases.append((n, arr))
    
results = calc(t, test_cases)
for res in results:
    print(res)