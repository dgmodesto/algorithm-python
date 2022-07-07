# https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

# INPUT
# this is a string

# OUTPUT
# this-is-a-string

def split_and_join(line):
    # write your code here
    a = line.split();
    return "-".join(a)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
    