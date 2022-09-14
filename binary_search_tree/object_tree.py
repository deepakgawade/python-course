#objecct can be store in key and object as value.
class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.right = self.left=self.parent=None
        pass
class User:
    def __init__(self,username,name,email):
        self.username=username
        self.name=name
        self.email=email
        pass

if __name__=="__main__":
    jandesh=User('jandesh','Jandesh Tulaskar', 'jandesh@gmail.com')
    binidya=User('bindiya','Bindiya kansekar', 'biniya@gmail.com')
    sonaksh=User('sonaksh', 'Sonkshi Sinha', 'sonksh@gmail.com')
    tree=BSTNode(jandesh.username,jandesh)
    tree.left=BSTNode(binidya.username,binidya)
    tree.right=BSTNode(sonaksh.username,sonaksh)

    print('{} \n {}\n{}'.format(tree.value,tree.left.value.name,tree.right.value.name))

    pass
