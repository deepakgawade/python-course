class TreeNode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
        
if __name__=="__main__":
    def parse_tuple(data):
        print(data)
        if isinstance(data,tuple) and len(data)==3:
            node =TreeNode(data[1])
            node.left=parse_tuple(data[0])#here te recursion will start.
            node.right=parse_tuple(data[2])#same here
        elif data is None:#this is stoping conditon if tere is no data at leaf we want call parse_tuple again.
            node=None
        else:
            node=TreeNode(data)
        return node
    tree_tuple=((1,3,None),2,((None,3,4),5,(6,7,8)))
    tree1=parse_tuple(tree_tuple)

    def traverse_preorder(node):
        if node is None:
            return []
        return (  [node.key] + traverse_preorder(node.left) + traverse_preorder(node.right))
    

    def traverse_inorder(node):
        if node is None:
            return []
        return (traverse_inorder(node.left) + [node.key]+traverse_inorder(node.right))

    def traverse_postorder(node):
        if node is None:
            return []
        return (traverse_postorder(node.left) + traverse_postorder(node.right) + [node.key])

    traverse_data=traverse_postorder(tree1)
    print(traverse_data)
    name=[22] + [45]
    print(name)
    pass