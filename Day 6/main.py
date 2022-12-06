#!/usr/bin/python3

def solve(data):
    # Part 1 and 2
    return search(data, 4), search(data, 14)

def search(data: str, n: int) -> int:
    """Search for first instance of non-matching n digit character markers"""
    for i in range(len(data[n - 1:])):
        if n == len(set(data[i:i + n])):
            return i + n

if __name__ == '__main__':
    testing = False
    with open('testinput.txt' if testing else 'input.txt') as f:
        data = f.read().splitlines()[0]  # Data contains only one line in this specific problem

    ans = solve(data)
    print(f"Part 1 Solution: {ans[0]}")
    print(f"Part 2 Solution: {ans[1]}")