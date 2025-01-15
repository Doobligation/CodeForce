# A+B

def calc(x):
    return x[0] + x[1]

test = calc(list(map(int, (input().split()))))

print(test)