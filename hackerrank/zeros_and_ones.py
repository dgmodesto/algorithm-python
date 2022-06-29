# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# INPUT
# 3 3 3


# OUTPUT
# [[[0 0 0]
  # [0 0 0]
  # [0 0 0]]
# 
#  [[0 0 0]
  # [0 0 0]
  # [0 0 0]]
# 
#  [[0 0 0]
  # [0 0 0]
  # [0 0 0]]]
# [[[1 1 1]
  # [1 1 1]
  # [1 1 1]]
# 
#  [[1 1 1]
  # [1 1 1]
  # [1 1 1]]
# 
#  [[1 1 1]
  # [1 1 1]
  # [1 1 1]]]

import numpy

arr = input()
print(numpy.zeros((numpy.array(arr.split(), int)), int))
print(numpy.ones((numpy.array(arr.split(), int)), int))


