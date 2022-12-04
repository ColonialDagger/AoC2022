#!/usr/bin/python3

def solve(data):
    ans1 = 0
    ans2 = 0
    for i in data:
        i = i.split(',')
        i[0] = list(map(int, i[0].split('-')))
        i[1] = list(map(int, i[1].split('-')))

        # Part 1
        # Finds sets where all elements of one set are contained in the other set
        if (
            (i[0][0] <= i[1][0] and i[0][1] >= i[1][1]) or
            (i[1][0] <= i[0][0] and i[1][1] >= i[0][1])
        ):
            ans1 += 1

        # Part 2
        # Finds sets that have any elements overlapping each other
        if (
            i[0][0] <= i[1][0] <= i[0][1] or
            i[0][0] <= i[1][1] <= i[0][1] or
            i[1][0] <= i[0][1] <= i[1][1] or
            i[1][0] <= i[0][1] <= i[1][1]
        ):
            ans2 += 1

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
