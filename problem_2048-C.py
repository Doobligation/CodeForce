# Kevin and Binary Strings
def calc(t, test_cases):
    results = []

    # for num in test_cases:
    #     r_2 = 1
    #     l_2 = 1

    #     maximum_num = int("1", 2)


        # for i in range(len(num)):
        #     j = len(num)

        #     while(i < j):
        #         start = 0 + i 
        #         end = j

        #         temp = num[start:end]

        #         res = int(num, 2) ^ int(temp, 2)

        #         if(maximum_num < res):
        #             r_2 = i + 1
        #             l_2 = j
        #             maximum_num = max(maximum_num, res)
        #         j -= 1

        # results.append([1, len(num), r_2, l_2])

    for num in test_cases:
        maximum_num = int("1", 2)
        r_2 = 1
        l_2 = 1
        for i in range(len(num)):
            for j in range(i + 1, len(num) + 1):
                res = int(num, 2) ^ int(num[i:j], 2)

                if(maximum_num < res):
                    r_2 = i + 1
                    l_2 = j
                    maximum_num = res

        results.append([1, len(num), r_2, l_2])

    return results
        


t = int(input())
test_cases = []

for _ in range(t):
    test_cases.append(str(input()))

results = calc(t, test_cases)

# print(results)
for res in results:
    print(" ".join(list(map(str, res))))

