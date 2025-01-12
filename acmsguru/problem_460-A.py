# Plural Form of Nouns

def calc(t, test_cases):
    results = []

    for word in test_cases:
        temp = list(word)
        new_word = ""

        if (temp[-1] == "x" or
            temp[-1] == "s" or
            temp[-1] == "o"
            ):
                temp.append("es")
            
        elif (temp[-1] == "f"):
                temp[-1] = "ves"
        
        elif (temp[-1] == "y"):
                temp[-1] = "ies"
        
        elif (temp[-2:] == ["c", "h"]):
            temp.append("es")

        elif (temp[-2:] == ["f", "e"]):
            temp.pop()
            temp.pop()
            temp.append("ves")

        else: 
            temp.append("s")



        new_word = "".join(temp)
        results.append(new_word)

    return results



t = int(input())
test_cases = []

for _ in range(t):
    n = str(input())
    test_cases.append(n)

results = calc(t, test_cases)

for res in results:
    print(res)
