def solve(data):
    # Part 1
    score = 0
    for i in data:
        opp = i[0]  # Opponent
        pla = i[2]  # Player
        if opp == 'A':
            if pla == 'X':
                score += 4
            if pla == 'Y':
                score += 8
            if pla == 'Z':
                score += 3
        if opp == 'B':
            if pla == 'X':
                score += 1
            if pla == 'Y':
                score += 5
            if pla == 'Z':
                score += 9
        if opp == 'C':
            if pla == 'X':
                score += 7
            if pla == 'Y':
                score += 2
            if pla == 'Z':
                score += 6

    ans1 = score

    # Part 2
    score = 0
    for i in data:
        opp = i[0]  # Opponent
        pla = i[2]  # Player
        if opp == 'A':
            if pla == 'X':
                score += 3
            if pla == 'Y':
                score += 4
            if pla == 'Z':
                score += 8
        if opp == 'B':
            if pla == 'X':
                score += 1
            if pla == 'Y':
                score += 5
            if pla == 'Z':
                score += 9
        if opp == 'C':
            if pla == 'X':
                score += 2
            if pla == 'Y':
                score += 6
            if pla == 'Z':
                score += 7
    ans2 = score

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