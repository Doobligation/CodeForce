#include <bits/stdc++.h>
using namespace std;

/**
 * Remove leading zeros from a binary string, except keep at least one '0' if the number is zero.
 */
string stripLeadingZeros(const string &bin) {
    // Find first '1'
    size_t pos = bin.find_first_not_of('0');
    if (pos == string::npos) {
        // means all zeros
        return "0";
    }
    return bin.substr(pos);
}

/**
 * Compare two binary strings by integer value.
 * Return:
 *   -1 if A < B
 *    0 if A == B
 *   +1 if A > B
 */
int compareBinaryStrings(const string &A, const string &B) {
    // Remove leading zeros before comparing
    string a = stripLeadingZeros(A);
    string b = stripLeadingZeros(B);

    // First compare lengths
    if (a.size() < b.size()) return -1;
    if (a.size() > b.size()) return +1;

    // If same length, compare lexicographically
    if (a == b) return 0;
    return (a < b) ? -1 : +1;
}

/**
 * XOR two binary strings (possibly different lengths), return the binary string result.
 * 1. Zero-pad the shorter string on the left so lengths match.
 * 2. Perform bitwise XOR.
 * 3. Strip leading zeros.
 * 4. If empty, return "0".
 */
string xorBinaryStrings(const string &A, const string &B) {
    // Strip leading zeros from inputs to minimize padding but still correct
    string a = stripLeadingZeros(A);
    string b = stripLeadingZeros(B);

    // Pad the shorter one
    if (a.size() < b.size()) {
        a.insert(a.begin(), b.size() - a.size(), '0');
    } else if (b.size() < a.size()) {
        b.insert(b.begin(), a.size() - b.size(), '0');
    }

    // Now a.size() == b.size()
    string result;
    result.reserve(a.size());
    for (size_t i = 0; i < a.size(); i++) {
        if (a[i] == b[i]) {
            result.push_back('0');
        } else {
            result.push_back('1');
        }
    }

    // Strip leading zeros from the result
    string finalRes = stripLeadingZeros(result);
    return finalRes;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    // Vector to store results for each test case
    vector<array<int,4>> results;
    results.reserve(t);

    while (t--) {
        string num;
        cin >> num;

        // The original Python code sets:
        //   r1 = 1, l1 = len(num)
        //   r2 = 1, l2 = 1
        //   maximumNum = int("1", 2) = 1  (as a decimal)
        // We'll keep them as is. But "maximumNum" is a binary string "1".
        int r1 = 1;
        int l1 = (int)num.size();
        int r2 = 1;
        int l2 = 1;

        // We'll treat num as a binary string; no conversion to integer type.
        // Let "numAll" = the whole string
        string numAll = num;

        // Initialize maximumNum as binary string "1"
        string maximumNum = "1";

        // The nested loops from the Python code:
        // for i in range(len(num)):
        //     j = len(num)
        //     while i < j:
        //         temp = num[i:j]
        //         res = int(num,2) ^ int(temp,2)
        //         if (res > maximum_num):
        //             ...
        //         j -= 1
        //
        // Here we do the same but with string-based XOR.

        int n = (int)num.size();
        for (int i = 0; i < n; i++) {
            int j = n;
            while (i < j) {
                // substring = num[i:j]
                // length is j-i
                string subStr = num.substr(i, j - i);

                // XOR with the entire string
                string res = xorBinaryStrings(numAll, subStr);

                // compare with maximumNum
                if (compareBinaryStrings(res, maximumNum) > 0) {
                    // If res is bigger, update indices and maximumNum
                    r2 = i + 1; // 1-based index for start
                    l2 = j;     // j is already 1-based end
                    maximumNum = res;
                }
                j--;
            }
        }

        // We always output r1, l1, r2, l2
        results.push_back({r1, l1, r2, l2});
    }

    // Output the results
    for (auto &res : results) {
        cout << res[0] << " " << res[1] << " "
             << res[2] << " " << res[3] << "\n";
    }

    return 0;
}
