# Fibonacciness
# import math

def calc(t, test_cases):
    results = []

    for case in test_cases:
        temp = []
        count = 0

        a_1 = case[0]
        a_2 = case[1]
        a_4 = case[2]
        a_5 = case[3]

        temp.append(a_1 + a_2)
        temp.append(a_4 - a_2)
        temp.append(a_5 - a_4)

        temp2 = []

        for x in range(len(temp)):
            if temp[x] not in temp2:
                temp2.append(temp[x])
                count += 1

        results.append(abs(count - 4))

    return results
            


t = int(input())
test_cases = []

for _ in range(t):
    a, b, c, d = map(int, input().split())
    test_cases.append([a, b, c, d])

results = calc(t, test_cases)

for res in results:
    print(res)