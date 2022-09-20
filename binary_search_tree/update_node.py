import insert_node  

class TreeNode:
    def __init__(self,key):
        self.key=key
        self.right=self.left=None

if __name__== "__main__":
    def find_node(node,key):

        if node is None:
            return None

        if node.key==key:
            return node
        
        if node.key<key:
            return find_node(node.right,key)
        if node.key>key:
            return find_node(node.left,key)


    def update_node(node, key, value):

        target=find_node(node,key)

        if target is not None:
            target.key=value
            print("value updated")



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

    update_node(tree1,5,22)

    insert_node.display_keys(tree1)

    node=find_node(tree1,9)
    if node is None:
        print("Sorry, its not here")
    else: 
        print(node)
