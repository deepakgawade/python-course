class Node:
    def __init__(self,data):
        self.key=data
        self.left=self.right=None

if __name__=="__main__":
    def parse_tuple(data):
       # print(data)
        if isinstance(data,tuple) and len(data)==3:
            node =Node(data[1])
            node.left=parse_tuple(data[0])#here te recursion will start.
            node.right=parse_tuple(data[2])#same here
        elif data is None:#this is stoping conditon if tere is no data at leaf we want call parse_tuple again.
            node=None
        else:
            node=Node(data)
        return node
    def remove_none(nums):
        return [x for x in nums if x is not None]

    def is_bst(node):
        if node is None:
            return True,None,None

        #check if the left sub tree is BST and right sub tree is BST
        is_bst_l, min_l, max_l = is_bst(node.left)
        is_bst_r, min_r, max_r = is_bst(node.right)

        is_bst_node = ( is_bst_l and is_bst_r and 
                        (max_l is None or node.key>max_l) 
                        and (min_r is None or node.key<min_r))
        min_key = min(remove_none([min_l, node.key,min_r]))
        max_key = max(remove_none([max_l,node.key,max_r]))
       # print(node.key, max_key, min_key)

        return is_bst_node, min_key, max_key



    tree1 = parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))
    tree2 = parse_tuple((('aakash', 'biraj', 'hemanth')  , 'jadhesh', ('siddhant', 'sonaksh', 'vishal')))

    a,b,c= is_bst(tree2)
    print("this is the node {} {} {}".format(a,b,c))

