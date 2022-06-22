# https://www.hackerrank.com/challenges/np-concatenate/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# INPUT
# 4 3 2
# 1 2
# 1 2 
# 1 2
# 1 2
# 3 4
# 3 4
# 3 4 


# OUTPUT
# [[1 2]
#  [1 2]
#  [1 2]
#  [1 2]
#  [3 4]
#  [3 4]
#  [3 4]] 

import numpy


n, m, p = numpy.array(input().split(' '), int)
arr = numpy.array(input().strip().split(), int)

for i in range(1, n+m):
    arr = numpy.vstack((arr, numpy.array(input().strip().split(), int)))

    
print(arr)