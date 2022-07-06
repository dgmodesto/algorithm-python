# https://www.hackerrank.com/challenges/python-tuples/problem?isFullScreen=true

# INPUT
# 2
# 1 2


# OUTPUT
# 3713081631934410656

# print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])

if __name__ == '__main__':
  n = int(input())
  integer_list =  map(int, input().split())
  
  t = tuple(integer_list)
  print(hash(t))
  
  
  