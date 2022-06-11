
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

# Este método olhar primeiro para os nós da esquerda, direita e por ultimo olha pra si
  def postorder_traversal(self, node=None):
    if node is None:
      node = self.root
    if node.left:
      self.postorder_traversal(node.left)
    if node.right:
      self.postorder_traversal(node.right)

    print(node.data)

  def height(self, node=None):
    if node is None:
        node = self.root

    hleft = 0
    hright = 0

    if node.left:
        hleft = self.height(node.left)
    if node.right:
        hright = self.height(node.right)
    if hright > hleft:
      return hright + 1
    return hleft + 1

