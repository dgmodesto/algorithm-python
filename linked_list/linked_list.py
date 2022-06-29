from re import I
from node import Node 

class LinkedList:
  def __init__(self):
    self.head = None
    self._size = 0

  def append(self, element):
    node = Node(element)
    if self.head:
      #insert when the list there are elements
      pointer = self.head
      while pointer.next:
        pointer = pointer.next

      pointer.next = node 
    else:
      #first insertion
      self.head = node 
    self._size = self._size + 1
      
  def __len__(self):
    '''Return the list size'''
    return self._size
  
  def get(self, index):
    pass
  
  def __getitem__(self, index):
    pointer = self.head
    for i in range(index):
      if pointer:
        pointer = pointer.next
      else: 
        raise IndexError('List index out of range')
        
    if pointer:
      return pointer.data 
    else : 
      raise IndexError('List index out of range')
  
  def __setitem__(self, index, element):
    pointer = self.head
    for i in range(index):
      if pointer:
        pointer = pointer.next
      else: 
        raise IndexError('List index out of range')
        
    if pointer:
      pointer.data = element 
    else : 
        raise IndexError('List index out of range')
  
  def index(self, element):
    '''return the index of element list'''
    pointer = self.head
    i = 0
    while pointer:
      if pointer.data == element:
        return i
      pointer = pointer.next
      i = i + 1
      
    raise ValueError('{} is not in list'.format(element))