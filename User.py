class User:
    user_count=0

    def __init__(self,username,email):
        self.username=username
        self._email=email
        User.user_count+=1 #this is a static attribute

    def dispaly_User(self):
        print(f'Username: {self.username} and Email: {self._email}')

    

user1=User("Arnab","arnabkundu759@gmail.com")
user2=User("Bijoy","bijoykar54321@gmail.com")
user3=User("Sannik","sannikbej456@gmail.com")


print(User.user_count)
user1.dispaly_User()
user2.dispaly_User()