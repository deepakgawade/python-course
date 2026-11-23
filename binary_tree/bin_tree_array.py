from collections import deque

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right  


def build_tree_from_array(arr, i=0, depth=0):
    print(" " * depth + f"i={i}")
    if i >= len(arr) or arr[i] is None:
        print(" "* depth + "->None")
        return None
    return Node(arr[i], build_tree_from_array(arr, 2*i+1, depth+1), build_tree_from_array(arr, 2*i+2, depth+1))


def level_order(root):
    if not root:
        return []
    res, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            n = q.popleft()
            level.append(n.value)
            if n.left:q.append(n.left)
            if n.right:q.append(n.right)
        res.append(level)

    return res 

def inorder(root, out):
    if not root:
        return 
    inorder(root.left, out)
    out.append(root.value)
    inorder(root.right, out)

def postorder(root, out):
    if not root:
        return
    postorder(root.left,out)
    postorder(root.right, out)
    out.append(root.value)


def preorder(root, out):
    if not root:
        return
    out.append(root.value)
    preorder(root.left, out)
    preorder(root.right,out)



if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9]
    root = build_tree_from_array(arr)
    print(level_order(root))  # Output: [[1], [2, 3], [4, 5, 6]]
    out = []
    inorder(root, out)
    print(f"inorder trvaersal result:", out)
    out =[]
    preorder(root, out)
    print(f"preorder traversal result:", out)
    out = []
    postorder(root, out)
    print(f"postorder traversal result:", out)
