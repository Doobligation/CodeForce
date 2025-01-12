# Theatre Square

import math

def calc(zone):

    vertical = (zone[0] + zone[2] - 1) // zone[2]
    horizontal = (zone[1] + zone[2] -1) // zone[2]

    return int(vertical * horizontal)

nani = list(map(int, input().split()))
print(calc(nani))