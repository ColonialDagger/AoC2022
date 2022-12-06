#!/usr/bin/python3

def solve(data):
    # Part 1 and 2
    # Search for first instance of non-matching n digit character markers
    return search(data, 4), search(data, 14)

def search(data: str, n: int) -> int:
    for i in range(data[n - 1:].__len__()):
        if data[i:i + n].__len__() is set(data[i:i + n]).__len__():
            return i + n

if __name__ == '__main__':
    testing = False

    # Reads lines into a list input
    print('Counting data...')
    file = 'testinput.txt' if testing else 'input.txt'
    with open('testinput.txt' if testing else 'input.txt') as f:
        data = f.read().splitlines()[0]  # Data contains only one line in this specific problem

    ans = solve(data)
    print(f"Part 1 Solution: {ans[0]}")
    print(f"Part 2 Solution: {ans[1]}")