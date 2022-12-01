def solve(data):
    # Part 1
    cal = []
    n = 0
    for i in data:
        if i == '\n':
            cal.append(n)
            n = 0
        else:
            n += int(i)
    ans1 = max(cal)

    # Part 2
    cal.sort()
    ans2 = sum(cal[-3:])

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