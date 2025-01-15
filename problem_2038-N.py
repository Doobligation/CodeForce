# Fixing the Expression
def calc(t, test_cases):
    results = []

    for case in test_cases:
        string = list(case)
        # if string[1] == "=":
        #     comp = bool(string[0] == string[2])
        #     if not comp:
        #         string[0] = string[2]

        # elif string[1] == ">":
        #     comp = bool(string[0] > string[2])
        #     if not comp:
        #         string[1] = "<"

        # else:
        #     comp = bool(string[0] < string[2])
        #     if not comp:
        #         string[1] = ">"

        if string[0] == string[2]:
            string[1] = "="
        elif string[0] > string[2]:
            string[1] = ">"
        else:
            string[1] = "<"
            
        results.append("".join(string))
    
    return results


t = int(input())
test_cases = []

for _ in range(t):
    test_cases.append(input())

results = calc(t, test_cases)

for res in results:
    print(res)