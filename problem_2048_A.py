# Kevin and Combination Lock

def calc(t, test_cases):
    results = []

    # for num in test_cases:
    #     res = int(num)

    #     while res > 0:
    #         digits = [int(digit) for digit in str(res)]     
    #         x= 0

    #         while x < len(digits) - 1:
    #             if digits[x] == 3 and digits[x+1] == 3:
    #                 digits.pop(x)
    #                 digits.pop(x)
    #                 # Reset `x` to recheck from the beginning after modification
    #                 x = max(0, x - 1)
    #             else:
    #                 x += 1
            
    #         res = int("".join(map(str, digits))) if digits else 0
    #         res -= 33

    #     if res == -33:
    #         results.append("yes")
    #     else:
    #         results.append("no")



    # for num in test_cases:
    #     if num % 33 == 0:
    #         results.append("yes")
    #     else:
    #         results.append("no")


    for num in test_cases:
        num_str = str(num)
        while "33" in num_str:
            num_str = num_str.replace("33", "")

        if num_str == "" or int(num_str) % 33 == 0:
            results.append("yes")
        else:
            results.append("no")

    
    return results



t = int(input());
test_cases = []

for _ in range(t):
    test_cases.append(int(input()))

results = calc(t, test_cases)

for res in results:
    print(res)