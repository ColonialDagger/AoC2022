def solve(data):
    # Part 1
    ans1 = 0
    ruleset = {
        'A': {'X': 4, 'Y': 8, 'Z': 3},
        'B': {'X': 1, 'Y': 5, 'Z': 9},
        'C': {'X': 7, 'Y': 2, 'Z': 6},
    }
    for i in data:
        ans1 += ruleset[i[0]][i[2]]

    # Part 2
    ans2 = 0
    ruleset = {
        'A': {'X': 3, 'Y': 4, 'Z': 8},
        'B': {'X': 1, 'Y': 5, 'Z': 9},
        'C': {'X': 2, 'Y': 6, 'Z': 7},
    }
    for i in data:
        ans2 += ruleset[i[0]][i[2]]

    return ans1, ans2

if __name__ == '__main__':
    testing = False

    # Reads lines into a list input
    print('Counting data...')
    file = 'testinput.txt' if testing else 'input.txt'
    with open(file) as f:
        data = f.readlines()

    ans = solve(data)
    print(f"Part 1 Solution: {ans[0]}")
    print(f"Part 2 Solution: {ans[1]}")