from platform import node


class TreeNode:
    def __init__(self,key) -> None:
        self.key=key
        self.left=None
        self.right=None
        
if __name__== "__main__":
    def parse_tupple(data):
        if isinstance(data,tuple) and len(data)==3:
            node = TreeNode(data[1])
            node.left=parse_tupple(data[0])
            node.right=parse_tupple(data[2])
        elif data is None:
            node=None
        else:
            node=TreeNode(data)
        return node


    def minDepth(root):

        if root is None:
            return 0
        
        #create a empty queue
        q=[]
        q.append({'node':root,'depth':1})

        # level order traversal
        while(len(q)>0):
            queueItem=q.pop(0)
            
            node=queueItem['node']
            depth=queueItem['depth']

            if node.left is None and node.right is None:
                return depth
            
            if node.left is not None:
                q.append({'node':node.left,'depth':depth+1})
            
            if node.right is not None:
                q.append({'node':node.right,'depth':depth+1})
    tree_tuple=((1,3,None),2,((None,3,4),5,(6,7,8)))
    tree_tuple2=((None),2,(None,5,(None,7,(None,55,(None,0,6)))))

    tree1=parse_tupple(tree_tuple2)
    print(tree1)
    value=minDepth(tree1)
    print(value)




    