# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

# INPUT
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39

# OUTPUT
# Berry
# Harry


if __name__ == '__main__':
    lst = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append([name, score])
        
    i = 0
    lowest = 0
    newList = sorted(lst,key= lambda x: x[1])
    second_lowest = []
    for sub in newList:
        if i > 0 and float(sub[1]) > lowest:
            for j in newList:
                if j[1] == sub[1]:
                    second_lowest.append(j)
            break
        lowest = float(sub[1])
        i = i + 1
        
    second_lowest.sort()
    for name in second_lowest:
        print(name[0])