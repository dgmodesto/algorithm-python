# Last inserted, first removed 
# O(1)


# insert in stack
# remove from stack
#to see on the top of stack
from node import Node


class Queue:
  def __init__(self):
    self.first = None
    self.last = None 
    self._size = 0

  def push(self, element):
    #insert a element in stack
    node = Node(element)
    if self.last is None:
      self.last = node
    else:
      self.last.next = node
      self.last = node

    if self.first is None:
      self.first = node

    self._size = self._size + 1


  def pop(self):
    #remove item from the top's stack
    if self._size > 0:
      elem = self.first.data
      self.first = self.first.next
      self._size = self._size - 1
      return elem
    raise IndexError("The queue is empty")

  def peek(self):
    #return the top without remove 
    if self._size > 0:
      elem = self.first.data
      return elem
    raise IndexError("The queue is empty")

  def __len__(self):
    #return the size of stack
    return self._size

  def __repr__(self):
    if self._size > 0:
      r = ""
      pointer = self.first
      while(pointer):
        r = r + str(pointer.data) + " "
        pointer = pointer.next
      return r
    else:
      raise IndexError("The queue is empty")


  def __str__(self):
    return self.__repr__()