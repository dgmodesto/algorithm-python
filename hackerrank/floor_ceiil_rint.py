import numpy as np

#https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
#Input
# 1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9

#Output
# [ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
# [  2.   3.   4.   5.   6.   7.   8.   9.  10.]
# [  1.   2.   3.   4.   6.   7.   8.   9.  10.]

numpy.set_printoptions(legacy='1.13')

arr = numpy.array(input().split(' '), float)

print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))

