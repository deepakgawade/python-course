class TreeNode:
    def __init__(self,key):
        self.key=key
        self.right=None
        self.left=None
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
    def height_tree(node):
        
        if node is None:
            return 0
            
        return 1 + max( height_tree(node.left),height_tree(node.right))
    height=height_tree(tree1)
    print("{}".format(height))

    def size_tree(node):
        if node is None:
            return 0
        return 1 + size_tree(node.left) + size_tree(node.right)

    size=size_tree(tree1)
    print("size of tree is {}".format(size))
    pass