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

    node0=TreeNode(3)
    node1=TreeNode(4)
    node2=TreeNode(5)
    #user2.introduceYourself("deepak")
print(node0.key)

node0.left=node1
node0.right=node2

tree=node0
print(tree.key)
print(tree.left.key)
print(tree.right.key)

