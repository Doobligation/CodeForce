# runner.py

import subprocess

def run_line_by_line():
    # 1. Paste your sample input into a triple‐quoted string
    test_input = """\
3
4 3
1 1
2 2
2 1
1 2
1 2
1 1
6 7
3 6
1 1
3 1
6 6
5 4
6 1
"""

    # 2. Split the string into individual lines
    lines = test_input.strip().splitlines()

    # 3. Start 'a.py' as a subprocess with pipes for stdin and stdout
    process = subprocess.Popen(
        ["python", "problem_2056-A.py"],     # or full path to 'a.py' if needed
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True               # ensures text (not bytes) mode
    )

    # 4. Feed the lines one by one as if typed interactively
    for line in lines:
        process.stdin.write(line + "\n")
        process.stdin.flush()

    # 5. Close stdin and capture the output
    output, errors = process.communicate()

    # 6. Print the output and errors
    print("=== Output ===")
    print(output)
    if errors:
        print("=== Errors ===")
        print(errors)

if __name__ == "__main__":
    run_line_by_line()
