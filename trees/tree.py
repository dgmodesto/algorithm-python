class Node:
  def __init__(self, data) :
    self.data = data
    self.left = None
    self.right = None


    def __str__(self):
        return str(self.data)


class BynaryTree:
  def __init__(self, data=None, node=None):
    if node:
      self.root = node
    elif data:
      node = Node(data)
      self.root = node
    else:
      self.root = None


  # Percurso em ordem simetrica (o correto é "inorder" em ingles)
  def simetric_traversal(self, node=None):
    if node is None:
      node = self.root
    
    if node.left:
      print('(', end='')
      self.simetric_traversal(node.left)

    print(node.data, end='')

    if node.right:
      self.simetric_traversal(node.right)
      print(')', end='')

    

  
if __name__ == "__main__":
    tree = BynaryTree()
    n1 = Node('a')
    n2 = Node('+')
    n3 = Node('*')
    n4 = Node('b')
    n5 = Node('-')
    n6 = Node('/')
    n7 = Node('c')
    n8 = Node('d')
    n9 = Node('e')

    n6.left = n7
    n6.right = n8
    n5.left = n6
    n5.right = n9
    n3.left = n4
    n3.right = n5
    n2.left = n1
    n2.right = n3
    
    tree.root = n2
    tree.simetric_traversal()


    # print()

    #      '+'
    #    /     \
    #  'a'      '*'
    #          /   \
    #        'b'    '-'
    #              /    \
    #            '/'    'e' 
    #           /   \
    #         'c'   'd'

    # (a + (b * ((c/d) - e)))