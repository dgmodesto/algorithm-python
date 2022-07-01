
from http import server


def search(list, elem):
  '''Return element index if exist or None with the element didn't exist in the list'''
  for i in range(len(list)):
    if list[i] == elem:
      return i 
  
  return None

# def binarySearch(list, elem):
#   mid = len(list) // 2

#   indice = None
#   if  list[mid] == elem:
#     return mid
#   elif(list[mid] > elem):
#     indice =binarySearch(list[:mid], elem);
#   elif list[mid] < elem:
#     indice =binarySearch(list[mid:], elem)
  
#   return indice


list_stranger = [2, 5, 8, 11, 16, 32, 54, 89, 93]
element = 32

index = binarySearch(list_stranger, element)

if index is not None:
  print('the element index {} is {}'.format(element, index))
else :
  print("The element {} did not exist in the list".format(element))