from trees.tree import Node

# insert in stack
# remove from stack
#to see on the top of stack
class Stack:
  def __init__(self):
    self.top = None
    self._size = 0

  def push(self, element):
    #insert a element in stack
    node = Node(element)
    node.next = self.top
    self.top = node
    self._size = self._size + 1

  def pop(self):
    #remove item from the top's stack
    if self._size > 0:
      node = self.top
      self.top = self.top.next
      self._size = self._size - 1 
      return node.data 
    raise IndexError('The stack is empty')

  def peek(self):
    #return the top without remove 
    if self._size > 0:
      return self.top.data 
    raise IndexError('The stack is empty')

  def __len__(self):
    #return the size of stack
    return self._size

  def __repr__(self):
    r = ""
    pointer = self.top
    while(pointer):
      r = r + str(pointer.data) + "\n"
      pointer = pointer.next
    return r 

  def __str__(self):
    return self.__repr__()