"""
::AVL Trees::

Supports operations:

add(value) - adds a node into the AVL tree; must then balance

search(value) - looks for a node in the value.
"""

class Node():
    def __init__(self, value, height, parent = None):
        self.value = value
        self.height = height
        self.left = None
        self.right = None
        self.parent = parent

class Avl():
    def __init__(self):
        self.root = None

    def rotateL(self, node):
        """
        Say we have a tree like:
            node            h
        n.left  n.right     h-1
        A    B  C     D     h-2

        After rotating we would get:
               n.right      h
            node     D      h-1
        n.left  C           h-2
        A    B              h-3
        
        n.left retains height, but n
        """
        height = lambda n : -1 if not n else n.height
        C = node.right.left
        R = node.right
        node.right = C
        node.height = max(height(R.left), height(node.left)) + 1
        node.parent = R
        R.left = node
        R.height = max(height(R.left), height(R.right)) + 1
        R.parent = None
        return R

    def rotateR(self, node):
        """
        Say we have a tree like:
            node
        n.left  n.right
        A    B  C     D

        After rotating we would get:
            n.left
            A    node
                 B  node.right
                    C        D
        """
        height = lambda n : -1 if not n else n.height
        B = node.left.right
        L = node.left
        node.left = B
        node.height = max(height(L.right), height(node.right)) + 1
        node.parent = L
        L.right = node
        L.height = max(height(L.left), height(L.right)) + 1
        L.parent = None
        return L

    def balance(self, node):
        """
        We balance by checking height:
        """
        if not node: return None
        height = lambda n : -1 if not n else n.height
        hdiff = height(node.left) - height(node.right)
        # Recompute balancing
        node.height = max(height(node.left), height(node.right)) + 1
        par = node.parent
        orig = node
        if hdiff > 1:
            if height(node.left.left) < height(node.left.right):
                node.left = self.rotateL(node.left)
            node = self.rotateR(node)
        elif hdiff < -1:
            if height(node.right.left) > height(node.right.right):
                node.right = self.rotateR(node.right)
            node = self.rotateL(node)
        # Go back up the tree
        if not par:
            self.root = node
        else:
            if par.left and orig == par.left:
                par.left = node
            else:
                par.right = node
            node.parent = par
        self.balance(par)

    def BSTAdd(self, value):
        if not self.root:
            self.root = Node(value, 0, None)
            return self.root
        # Add it like BST: 
        node = self.root
        # While the node is not @ the leaf,
        # Recursively choose left or right child to
        # traverse and create a new node at the leaf.
        while True:
            if node.value > value:
                if node.left:
                    node = node.left
                else: break
            else:
                if node.right:
                    node = node.right
                else: break
        to_insert = Node(value, 0, node)
        if node.value > value:
            node.left = to_insert
        else:
            node.right = to_insert
        return to_insert

    def addNode(self, value):
        node = self.BSTAdd(value)
        self.balance(node)

    def traverse(self, node, indent = ""):
        if not node:
            print(indent + "x:-1")
            return
        print(indent + str(node.value) + ":" + str(node.height))
        for c in [node.left, node.right]:
            self.traverse(c, indent + "    ")

    def search(self, val):
        def r(n):
            if not n: return False 
            if n.value > val:
                return r(n.left)
            elif n.value < val:
                return r(n.right)
            else:
                return True
        return r(self.root)

if __name__ == "__main__":
    avl = Avl()
    avl.addNode(3)
    avl.addNode(5)
    avl.addNode(4)
    avl.addNode(10)
    avl.addNode(1)
    avl.addNode(8)
    print("Answer")
    avl.traverse(avl.root)
    print(avl.search(5))
    print(avl.search(3))
    print(avl.search(9))


