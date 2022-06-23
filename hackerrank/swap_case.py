#   https://www.hackerrank.com/challenges/swap-case/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

# INPUT
# HackerRank.com presents "Pythonist 2".

# OUTPUT
# hACKERrANK.COM PRESENTS "pYTHONIST 2".


def swap_case(s):
    newString = ''
    for c in s:
        if c.isupper():
            newString += c.lower()
        else:
            newString += c.upper()
    return newString

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)