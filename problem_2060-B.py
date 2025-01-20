# Fibonacciness
# import math

def calc(t, test_cases):
    results = []

    for case in test_cases:
        not_consistent = False

        n, m = case[0][0], case[0][1]

        if m != 1 and n != 1:
            for x in range(1, n):
                for y in range(0, m-1):
                    minus = case[x][y] - case[x+1][y]
                    minus2 = (case[x][y+1] - case[x+1][y+1])
                    if minus != minus2:
                        not_consistent = True
                        break
        
        if not_consistent:
            results.append([-1])
            continue

        #Check case[1][x]
        kongs = []

        for x in range(1, n+1):
            kongs.append(case[x][0])

        sorted_index = [index + 1 for index, _ in sorted(enumerate(kongs), key=lambda x: x[1])]
        results.append(sorted_index)




    return results
            


t = int(input())
test_cases = []

for _ in range(t):
    temp = []

    n, m = map(int, input().split())
    temp.append([n,m])

    for x in range(n):
        inputs = list(map(int, input().split()))
        temp.append(inputs)
    
    test_cases.append(temp)

results = calc(t, test_cases)

for res in results:
    print(" ".join(map(str, res)))