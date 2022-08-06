#aS A SENIOR BACKEND engineer at jovian, you are tasked with developing a fast in memory data stucture to manage profile information (username, name and email) for 100 million users.
#  it should allow following operation to perform efficiently.
#1.Insertthe profile information for a new user.
#2.find the profile information of a user, given their username.
#3.update the profile information of user , with givaen username.
#4.List of all users of platform , sorted by username.

class User:
    def __init__(self, username, name, email):
        self.username=username
        self.name=name
        self.email=email
        print("User created")
    
    def introduceYourself(self, guest_name):
        print("Hi {}, I'm {}! Contact me at {}.".format(guest_name,self.name,self.email
        ))


if __name__=='__main__':
    user2=User("baka", "baka raav", "email@baka")
    user2.introduceYourself("deepak")

