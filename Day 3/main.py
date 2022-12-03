#!/usr/bin/python3

def solve(data):
    # Part 1
    ans1 = 0
    for i in data:
        for n in i[:int(i.__len__()/2)]:
            if n in i[int(i.__len__()/2):]:
                if n.isupper():
                    ans1 += ord(n)-38
                else:
                    ans1 += ord(n)-96
                break

    # Part 2
    ans2 = 0
    for i in range(0, int(data.__len__()/3)):
        group = data[i*3:i*3+3]
        for n in group[0]:
            if n in group[1] and n in group[2]:
                if n.isupper():
                    ans2 += ord(n)-38
                else:
                    ans2 += ord(n)-96
                break

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