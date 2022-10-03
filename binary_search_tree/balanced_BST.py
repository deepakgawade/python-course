#write afuction to determine if teree is balanced
#1.check if left subb tree is balanced 
#2. check if right sub tree is balanced.
#3,current node, ensure that the diffrence between the height of left subtree and right sub tree is not more than 1.abs(

class Node:
    def __init__(self, data):
        self.key=data
        self.right=self.left=None

if __name__=="__main__":

    def parse_tuple(data):
        if isinstance(data, tuple) and len(data)==3:
            node=Node(data[1])
            node.left=parse_tuple(data[0])
            node.right=parse_tuple(data[2])
        elif data is None:
            node=None
        else:
            node=Node(data)
        return node

    def is_balanced(node):
        if node is None:
            return True, 0
        balanced_l, height_l = is_balanced(node.left)
        balanced_r, height_r = is_balanced(node.right)

        balanced = balanced_l and balanced_r and abs(height_l-height_r)<=1 
        height =1+max(height_l,height_r)
        return balanced, height

    tree1 = parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, (3,55,(None,10,78))))))
    tree2 = parse_tuple((('aakash', 'biraj', 'hemanth')  , 'jadhesh', ('siddhant', 'sonaksh', 'vishal')))

    isbalanced , h = is_balanced(tree1)
    print("is balanced {}, height is {}".format(isbalanced, h))


    isbalanced , h = is_balanced(tree2)
    print("is balanced {}, height is {}".format(isbalanced, h))