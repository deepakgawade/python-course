class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

if __name__=="__main__":
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
        print(node.key, max_key, min_key)

        return is_bst_node, min_key, max_key

