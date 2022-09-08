from dataclasses import dataclass


class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None

class Height:
    def __init__(self):
        self.h=0



if __name__=="__main__":
    def  diameteropt(root, height):
    
    #store height of left and right tree
        lh=Height()
        rh=Height()

        #base codition- when biary is empty
        if root is None:
            height.h=0
            return 0
    
    #height of lef tsub tree and right subtree is obtained fronm
   # lh and rh and returned  value of function is stored in ldiameter and rdiameter
        ldiameter=diameteropt(root.left,lh) 
        rdiameter=diameteropt(root.right,rh)

    #height will be max of left sub tree and right subtree
        height.h=max(lh.h,rh.h) +1

    #returmn max of ld, rd and lh+rh+1
        return max(lh.h+rh.h+1,max(ldiameter,rdiameter))

#function to calculate diameter f binary tree
    def diameter(root):
        height = Height()
        return diameteropt(root, height)
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
    tree_tuple=((1,3,None),2,((None,3,4),5,(6,7,8)))
    tree_tuple2=((None),2,(None,5,(None,7,(None,55,(None,0,6)))))
    tree1=parse_tuple(tree_tuple)
    tree2=parse_tuple(tree_tuple2)

    print(diameter(tree1))


# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         result = [0]
#         def traverse(node):
#             if not node:
#                 return -1
#             left_height = traverse(node.left)
#             right_height = traverse(node.right)
#             result[0] = max(result[0], 2 + left_height + right_height)
            
#             return 1 + max(left_height, right_height)
        
#         traverse(root)
#         return result[0]
    