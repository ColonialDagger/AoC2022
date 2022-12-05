#!/usr/bin/python3

def solve(data):
    ans1 = ''
    ans2 = ''

    # Part 1
    # Sort stacked crates according to instructions given

    sep = data.index('')  # Line where data seperation occurs
    crates_init = ['']*int(data[sep-1][-1])  # Initial crates template
    instructions = data[sep+1:]
    for row in reversed(data[:sep-1]):  # Process crates input
        for n in range(len(row[1::4])):
            crates_init[n] = crates_init[n] + row[1::4][n] if row[1::4][n] != ' ' else crates_init[n]
    for (row, n) in zip(instructions, range(instructions.__len__())):  # Process instructions input
        row = row.split(' ')
        instructions[n] = [int(x) for x in row[1::2]]

    crates = crates_init[:]  # Active crates setup

    for row in instructions:  # Execute instructions
        n = row[0]  # Number of crates
        o = row[1]-1  # Origin
        d = row[2]-1  # Destination
        for i in range(n):
            crates[d] = crates[d] + crates[o][-1]
            crates[o] = crates[o][:-1]

    for stack in crates:  # Get top crate on each stack
        ans1 += stack[-1]

    # Part 2
    # Move crates in groups determined by instructions

    crates = crates_init[:]  # Reset crates to original
    for row in instructions:  # Execute instructions
        n = row[0]  # Number of crates
        o = row[1]-1  # Origin
        d = row[2]-1  # Destination
        crates[d] = crates[d] + crates[o][-n:]
        crates[o] = crates[o][:-n]

    for stack in crates:  # Get top crate on each stack
        ans2 += stack[-1]

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