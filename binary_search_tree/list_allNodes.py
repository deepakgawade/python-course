class Node:
    def __init__(self,key,value) -> None:
        self.key=key
        self.value=value
        self.right=self.left=None

class User:
    def __init__(self,username,name,email):
        self.username=username
        self.name=name
        self.email=email


if __name__== "__main__":
    jandesh=User('jandesh','Jandesh Tulaskar', 'jandesh@gmail.com')
    binidya=User('bindiya','Bindiya kansekar', 'biniya@gmail.com')
    sonaksh=User('sonaksh', 'Sonkshi Sinha', 'sonksh@gmail.com')
    radha=User('radha', 'radha Sinha', 'radha@gmail.com')
    seema=User('seema', 'seema Sinha', 'seema@gmail.com')
    subha=User('subha', 'subha Sinha', 'subha@gmail.com')

    #created object as value

    def insert_node(node,key,value):
        if node is None:
            node=Node(key,value)
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
    insert_node(tree,radha.username,radha)
    insert_node(tree,seema.username,seema)
    insert_node(tree,subha.username,subha)


    #list all nodes
    def list_all(node):

        if node is None:
            return []
        return list_all(node.left) +[node.key,node.value]+list_all(node.right)

    allNodes=list_all(tree)
    print(allNodes)


