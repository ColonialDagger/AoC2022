#!/usr/bin/python3

def solve(data):
    ans1 = 0
    ans2 = 0

    # Part 1
    # Search for first instance of non-matching 4 digit character markers
    for n in range(data[3:].__len__()):
        if data[n:n+4].__len__() is set(data[n:n+4]).__len__():
            ans1 = n+4
            break

    # Part 2
    # Search for first instance of non-matching 14 digit character markers
    for n in range(data[13:].__len__()):
        if data[n:n+14].__len__() is set(data[n:n+14]).__len__():
            ans2 = n+14
            break

    return ans1, ans2


if __name__ == '__main__':
    testing = False

    # Reads lines into a list input
    print('Counting data...')
    file = 'testinput.txt' if testing else 'input.txt'
    with open(file) as f:
        data = f.read().splitlines()[0]  # Data contains only one line in this specific problem

    ans = solve(data)
    print(f"Part 1 Solution: {ans[0]}")
    print(f"Part 2 Solution: {ans[1]}")