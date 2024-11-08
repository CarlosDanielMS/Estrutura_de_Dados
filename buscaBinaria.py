class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def busca_binaria(self, v):
        def busca_recursiva(node, v):
            if node is None:
                return False
            
            if node.value == v:
                return True
            elif v < node.value:
                return busca_recursiva(node.left, v)
            else:
                return busca_recursiva(node.right, v)
        
        return busca_recursiva(self, v)

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(10)

valor = 4
if root.busca_binaria(valor):
    print(f"O valor {valor} foi encontrado na árvore.")
else:
    print(f"O valor {valor} não foi encontrado na árvore.")

busca_binaria.py
