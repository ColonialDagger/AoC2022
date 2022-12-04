#!/usr/bin/python3

def solve(data):
    # Part 1
    # Finds the calorie count of the elf with the most calories
    cal = []
    n = 0
    for i in data:
        if i != '\n':
            n += int(i)
        else:
            cal.append(n)
            n = 0
    cal.append(n)
    ans1 = max(cal)

    # Part 2
    # Finds the calorie counts of the three elves with the most calories
    cal.sort()
    ans2 = sum(cal[-3:])

    return ans1, ans2

if __name__ == '__main__':
    testing = False

    # Reads lines into a list input
    print('Counting data...')
    file = 'testinput.txt' if testing else 'input.txt'
    with open(file) as f:
        data = f.read().splitlines()

    ans = solve(data)
    print(f"Part 1 Solution: {ans[0]}")
    print(f"Part 2 Solution: {ans[1]}")