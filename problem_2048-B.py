# Kevin and Permutation
    
def calc(t, test_cases):
    results = []
    
    for n, a in test_cases:
        temp = [0] * n
        numy = list(range(1, n+1))
        used = set()
        #set makes an unordered list? uses .add
    
        for x in range(1, n//a + 1):
            index1 = a*x - 1
            # index2 = temp.index(x)
            # # temp.index(x) takes O(n) of time -> inefficient
    
            # temp[index1], temp[index2] = temp[index2], temp[index1]

            temp[index1] = x
            used.add(x)
            
        numy_pointer = 0
        for i in range(n):
            if temp[i] == 0:  # Find empty slots in temp
                while numy[numy_pointer] in used:
                    numy_pointer += 1  # Skip used values
                temp[i] = numy[numy_pointer]
                used.add(numy[numy_pointer])

            
        results.append(temp)   
    
    return results
        
            
    
    
    
t = int(input())
test_cases = []
    
for _ in range(t):
    nani = tuple(map(int, input().split()))
    test_cases.append(nani)
    
results = calc(t, test_cases)
    
for res in results:
    print(" ".join(map(str, res)))