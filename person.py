from datetime import datetime

class Person:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    @property
    def email(self):
        print(f'Email accessed at {datetime.now()}')
        return self._email
    
    @email.setter
    def email(self,email):
        if '@' in email:
            self._email=email
            


    # def get_email(self):
    #     print(f'Email accessed at {datetime.now()}')
    #     return self._email
    
    # def clean_email(self):
    #     return self._email.strip().lower()
    
    # def set_email(self,email):
    #     if '@' in email:
    #         self._email=email

    def say_hello(self):
        print(f'Hello, my name is {self.username} and my email is {self.email}.')

    def say_hi_to_user(self,user):
        print(f'Hi {user.username}, my name is {self.username}.')
    

user1=Person("Arnab","arnab456@gmail.com","145623")
user2=Person("Bijoy","bijoy789@gmail.com","456822")


user1.say_hi_to_user(user2)

# print(user1.get_email())

# user1.set_email('Arnab789@gamil.com')

# print(user1.get_email())


print(user1.email)


