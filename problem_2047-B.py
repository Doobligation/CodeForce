# # Replace Character

# def calc(t, test_cases):
#     results = []

#     for n, s in test_cases:
#         least_count = len(set(s))
#         best_string = s
#         nani_string = s

#         for i in range(n):
#             for j in range(n):
#                 if i == j:
#                     continue

#                 temp = list(s)

#                 if temp[i] == temp[j]:
#                     continue

#                 temp[i] = temp[j]
#                 temp_string = "".join(temp)

#                 distinct = len(set(temp_string))

#                 if distinct < least_count:
#                     least_count = distinct
#                     best_string = temp_string
#                 elif s != temp_string:
#                     nani_string = temp_string
                    
#         if len(set(nani_string)) == len(set(best_string)):
#             results.append(nani_string)
#         else:
#             results.append(best_string)

#     return results


# t = int(input())
# test_cases = []

# for _ in range(t):
#     n = int(input())
#     s = input().strip()
#     test_cases.append((n,s))

# results = calc(t, test_cases)

# for res in results:
#     print(res)


import math

def solve():
    t = int(input().strip())
    
    # Precompute factorials up to 10 (since n <= 10)
    factorials = [math.factorial(i) for i in range(11)]

    for _ in range(t):
        n = int(input().strip())
        s = list(input().strip())  # Convert to list for easy modification

        # Edge case: if n == 1, there's no way to reduce permutations
        # (there is exactly 1 permutation no matter what).
        # The problem states we must do one operation, which won't change the string.
        if n == 1:
            print(''.join(s))
            continue

        # Calculate the # distinct permutations of original s (might be used for reference).
        # But we really only need the min over transformations.
        def distinct_permutations(arr):
            """Compute the number of distinct permutations of arr using freq formula."""
            freq = [0]*26
            for ch in arr:
                freq[ord(ch) - ord('a')] += 1
            # n! / (freq[a]! * freq[b]! * ...)
            num = factorials[len(arr)]
            for f in freq:
                if f > 1:
                    num //= factorials[f]
            return num

        best_string = None
        best_value = math.inf

        # Try all i, j
        for i in range(n):
            for j in range(n):
                # Temporarily change s[i] to s[j]
                original_char = s[i]
                s[i] = s[j]

                cur_value = distinct_permutations(s)
                if cur_value < best_value:
                    best_value = cur_value
                    best_string = s[:]

                # Revert the change
                s[i] = original_char

        print(''.join(best_string))

solve()