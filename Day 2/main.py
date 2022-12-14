#!/usr/bin/python3

def solve(data):
    # Part 1
    # Finds RPS score following the given strategy guide of what to play
    ans1 = 0
    ruleset = {
        ('A', 'X'): 4, ('A', 'Y'): 8, ('A', 'Z'): 3,
        ('B', 'X'): 1, ('B', 'Y'): 5, ('B', 'Z'): 9,
        ('C', 'X'): 7, ('C', 'Y'): 2, ('C', 'Z'): 6,
    }
    for i in data:
        ans1 += ruleset[i[0], i[2]]

    # Part 2
    # Finds RPS score following the given strategy guide of whether to win, lose, or draw
    ans2 = 0
    ruleset = {
        ('A', 'X'): 3, ('A', 'Y'): 4, ('A', 'Z'): 8,
        ('B', 'X'): 1, ('B', 'Y'): 5, ('B', 'Z'): 9,
        ('C', 'X'): 2, ('C', 'Y'): 6, ('C', 'Z'): 7,
    }
    for i in data:
        ans2 += ruleset[i[0], i[2]]

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