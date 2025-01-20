#Startup

def calc(t, test_cases):
    results = []

    for case in test_cases:
        print(case)
        n = case[0][0]
        k = case[0][1]

        dic = dict(case[0:])
        print(dic)


    return results



t = int(input())
test_cases = []
temp = []

for _ in range(t):
    temp.append(list(map(int, input().split())))
    for x in range(temp[0][1]):
        temp.append(list(map(int, input().split())))
    test_cases.append(temp)

results = calc(t, test_cases)

for res in results:
    print(res)
