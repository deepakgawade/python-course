#958. Check Completeness of a Binary Tree
#create queue. append a node. check node is null and return 
#move from left to right till reach th end and after end theri shuld not be any node.
#this only works if we move from left -> right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

if __name__=="__main__":
    def isCompleteTree(self, root):
        queuq=[root]
        i=0
        while queuq[i]:
            queuq.append(queuq[i].left)
            queuq.append(queuq[i].right)
            i=i+1
        return not any(queuq[i:])

    #create a tree using tupple and test the solution for completeness.
    #also add solution with DFS