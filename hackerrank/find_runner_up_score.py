
#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

# INPUT
# 5
# 2 3 6 6 5

# OUPUT
#  5


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    aAux = list(arr)
    aAux.sort(reverse=True)
    i = 0
    ru = 0
    for a in aAux:
        if i > 0 and ru > a :
            ru = a
            break
            
        ru = a  
        i = i + 1
        
    print(ru)