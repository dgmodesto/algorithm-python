# https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true

# INPUT
# abracadabra
# 5 k

# OUTPUT
# abrackdabra

def mutate_string(string, position, character):
    # return string[:position]+ character + string[position+1:]
    l = list(string);
    l[position] = character
    string = ''.join(l)
    return string


if __name__ == '__main__':
  s = input()
  i, c = input().split()
  s_new = mutate_string(s, int(i), c)
  print(s_new)