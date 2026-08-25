class User:

    def __init__(self,user_id,username):# triggers when object is created
        self.id=user_id
        self.username= username
        self.follower=0
        self.following=0

        # method 1: display user info

    def display_user(self):
        print(f"User ID: {self.id}")
        print(f"Username: {self.username}")

        # method 2: update username

    def change_username(self, new_username):
        self.username = new_username

_1=User("001","shruti")
_2=User("002","purva")
print(_2.username)
_2.display_user()
_2.change_username("shruts")
_2.display_user()
# print("new user being created")











# to avoid this thing we use constructor
# user_1=User() # user_1 is now a object
# user_1.id="001"
# user_1.username="shruti"
#
# print(user_1.username)
#
# user_2=User() # user_2 is a object
# user_2.number="002"
# user_2.username="purva"
#
# print(user_2.number)



######C O N S T R U C T O R###### used to initialize attribute

#SYNTAX

# class car():
#     def __init__(self):
#     # initialize attribute