# https://www.hackerrank.com/challenges/python-lists/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=7-day-campaign

# INPUT
# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print

# OUTPUT
# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

if __name__ == '__main__':
    N = int(input())
    l = []
    for n in range(N):
        s =  input().split()
        cmd = s[0]
        args = s[1:]
        if cmd !="print":
            cmd += "("+ ",".join(args) +")"
            eval("l."+cmd)
        else:
            print(l)