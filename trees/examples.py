from random import triangular
from tree import BynaryTree, Node

# Vídeo Implementando uma árvore binária: https://youtu.be/6E169kShoNU
def inorder_example_tree():
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
    return tree
    # tree.simetric_traversal()
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






def postorder_example_tree():
    tree = BynaryTree()
    n1 = Node('I')
    n2 = Node('N')
    n3 = Node('S')
    n4 = Node('C')
    n5 = Node('R')
    n6 = Node('E')
    n7 = Node('V')
    n8 = Node('A')
    n9 = Node('5')
    n11 = Node('-')
    n0 = Node('3')

    n0.left = n6
    n0.right = n9
    n6.left = n1
    n6.right = n5
    n5.left = n2
    n5.right = n4
    n4.right = n3
    n9.left = n8
    n9.right = n11
    n8.right = n7

    tree.root = n0
    return tree

    #          (3)
    #       /       \
    #     (E)       (5)
    #    /   \      /  
    #  (I)    (R)  (A)
    #        /   \    \
    #      (N)   (C)  (v)
    #               \
    #               (S)



if __name__ == "__main__":
    tree = postorder_example_tree()
    print("Percurso em pos ordem:")
    tree.postorder_traversal()
    print("Altura da avorve é :", tree.height())

# levelorder_traversal

    #         (61)
    #       /       \
    #     (43)       (89)
    #    /   \      /  
    #  (16)  (51)  (66)
    # /    \      \    \
#    (11)  (32)   (55)  (79)
    #                   /    \
    #                 (77)   (82)

#OUTPUT: 61 43 89 16 51 66 11 32 55 79 77 82
