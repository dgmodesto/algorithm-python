import random
from tree import BinarySearchTree, BynaryTree
random.seed(77)

def random_tree(size=42):
  values = random.sample(range(1, 1000), 42)
  bst = BinarySearchTree()
  for v in values:
    bst.insert(v)




def example_tree():
  values = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32, 100, 90]
  tree = BinarySearchTree()
  for v in values:
    tree.insert(v)
  return tree


bst = example_tree()
bst.levelorder_traversal()


# testar remoção da árvore
print('-----------------------------')
value = 100
print("Remover valor : " + str(value))
bst.remove(value)
print("Apos Remover {}".format(value))

print('\n -----------------------------')
bst.levelorder_traversal()
print('\n -----------------------------')

print("Maior valor da avorve é :", bst.max())
print("Menor valor da avorve é :", bst.min())


# print('-----------------------------')
# items = [1, 3, 981, 510, 1000]

# for item in items:
#   r = bst.search(item)
#   if r is None:
#     print(item, "não encontrado")
#   else:
#     print(r.root.data, "encontrado")