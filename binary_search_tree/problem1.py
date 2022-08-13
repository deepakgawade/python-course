#aS A SENIOR BACKEND engineer at jovian, you are tasked with developing a fast in memory data stucture to manage profile information (username, name and email) for 100 million users.
#  it should allow following operation to perform efficiently.
#1.Insertthe profile information for a new user.
#2.find the profile information of a user, given their username.
#3.update the profile information of user , with givaen username.
#4.List of all users of platform , sorted by username.

#class and methods
class User:
    def __init__(self, username, name, email):
        self.username=username
        self.name=name
        self.email=email
        print("User created")
    
    def introduceYourself(self, guest_name):
        print("Hi {}, I'm {}! Contact me at {}.".format(guest_name,self.name,self.email
        ))

class UserDatabase:
    def __init__(self):
        self.users=[]

    def insert(self,user):
        i=0
        while i< len(self.users):
            #find first username greater then new user name.
            if self.users[i].username>user.username:
                break
            i+=1
        self.users.insert(i, user)
    
    def find(self, username):
        for user in self.users:
            if user.username==username:
                return user
    
    def update(self, user):
        target=self.find(user.username)
        target.name,target.email=user.name,user.email

    def list_all(self):
        return self.users

    

#implemantaion of tree node
class TreeNode:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
    



if __name__=='__main__':
    # hemant=User("hemant", "baka raav", "email@baka")
    # Umesh=User("umesh", "umesh d", "umesh@baka")

    # Zarin=User("zarin", "zarin khan", "zarin@baka")

    # database= UserDatabase()
    # database.insert(hemant)
    # database.insert(Umesh)
    # database.insert(Zarin)
    # Zarin=User("zarin", "zarin k", "zarinkhan@baka")

    # database.update(Zarin)

    # allUsers=database.list_all()
    # for user in allUsers:

    #     print("User(username={},email={},name={})".format(user.username,user.email,user.name))

    # node0=TreeNode(2)
    # node1=TreeNode(3)
    # node2=TreeNode(5)
    # node3=TreeNode(1)

    # node4=TreeNode(3)

    # node5=TreeNode(7)

    # node6=TreeNode(4)
    # node7=TreeNode(6)
    # node8=TreeNode(8)


    # node0.left=node1
    # node1.left=node3

    # node0.right=node2
    # node2.left=node4
    # node4.right=node6

    # node2.right=node5
    # node5.left=node7
    # node5.right=node8

    # print(node0.key)

    # node0.right=node2
    # node0.left=node1

    # tree=node0
    # print(tree.key)
    # print(tree.left.key)
    # print(tree.right.key)

    #instead of using manual wa to create each node, why not use a tuple : which will save value in th form of pairs.
    tree_tuple=((1,3,None),2,((None,3,4),5,(6,7,8)))
    #Now to cerate a node we write a function adn use recurssuion to form whole tree.
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
    #user2.introduceYourself("deepak")
    tree1 =parse_tuple(tree_tuple)

    print("".format(tree1.left.key
    ))
    print("this is left most node {}".format(tree1.right))


    def tree_to_tuple(treeData):
        
        #tupleData=(left,key,right)
        if treeData is None:
            return None
            #(left,key,right)=tree_to_tuple(treeData.left),treeData.key,  tree_to_tuple(treeData.right)
        if treeData.left is None and treeData.right is None:
            return treeData.key
        

        return tree_to_tuple(treeData.left),treeData.key,tree_to_tuple(treeData.right)
    data=tree_to_tuple(tree1)
    print(data)
    
#after running code it will print data in following manner
# ((1, 3, None), 2, ((None, 3, 4 ), 5, (6, 7, 8)))
# (1, 3, None)
# 1

# None
# ((None, 3, 4), 5, (6, 7, 8))
# (None, 3, 4)
# None
# 4
# (6, 7, 8)
# 6
# 8
    #helper fuction for displayig tree for easier visuallization.
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
    display_keys(tree1,'  ')
        
tupple2=(((7,8,(6,67,10)),11,56),15,(60,65,(None,70,(67,81,100))))

tree2=parse_tuple(tupple2)

display_keys(tree2)

 







