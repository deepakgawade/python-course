#for inserting a node we first start from root node, compare the key and given value to be inserted,
# if value is smaller tham left subtree key then recursively insert into left sub tree .if node is none add the value to that node.
# if value is greater then right sub tree key then recursiveky insert into right sub tree,if node is none add value to that node.
# 

from unicodedata import name


class BSTNode:
    def __init__(self,key,value=None):
        self.key=key
        self.value=value
        self.right=self.left=self.parent=None
        
class User:
    def __init__(self,username,name,email):
        self.username=username
        self.name=name
        self.email=email

if __name__=="__main__":
    jandesh=User('jandesh','Jandesh Tulaskar', 'jandesh@gmail.com')
    binidya=User('bindiya','Bindiya kansekar', 'biniya@gmail.com')
    sonaksh=User('sonaksh', 'Sonkshi Sinha', 'sonksh@gmail.com')
    #created object as value

    def insert_node(node,key,value):
        if node is None:
            node=BSTNode(key,value)
        elif key< node.key:
            node.left=insert_node(node.left,key,value)
            node.left.parent=node
        elif key>node.key:
            node.right=insert_node(node.right,key,value)
            node.right.parent=node

        return node
    
    #start inserting node
    tree=insert_node(None, jandesh.username,jandesh)
    insert_node(tree, binidya.username,binidya)
    insert_node(tree,sonaksh.username,sonaksh)

    def display_keys(node, space='\t', level=0):
        #print(node.key if node else None,level)
        #if node is empty
        if node is None:
            print(space*level+'@')
            return
        #if node is a leaf
        if node.left is None and node.right is None:
            print(space*level+ str(node.key))
            return
        #if the node has children
        display_keys(node.right, space,level+1)
        print(space*level+str(node.key))
        display_keys(node.left, space, level+1)

    display_keys(tree)
    