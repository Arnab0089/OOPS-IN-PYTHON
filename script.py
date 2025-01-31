name='Arnab'
age=21

print(f'My name is {name} and I am {age} years old.')
print(type(name))
print(type(age))


class Dog:
    def __init__(self,name,breed,owner):
        self.name=name
        self.breed=breed
        self.owner=owner

    def bark(self):
        print('Woof! Woof!')

class Owner:
    def __init__(self,name,address,contact_number,dog):
        self.name=name
        self.dog=dog
        self.address=address
        self.phone_number=contact_number


owner1=Owner("Arnab","Shirampore","1234567890","Tommy")
dog1= Dog("Tommy","German Shepherd",owner1)

owner2=Owner("Rahul","Kolkata","1234567890","Buddy")
dog2= Dog("Buddy","Golden Retriever",owner2)

print(f'{dog1.name} is a {dog1.breed} and its owner is {dog1.owner.name} and his address is {dog1.owner.address} and his phone number is {dog1.owner.phone_number}')
print(f'{dog2.name} is a {dog2.breed} and its owner is {dog2.owner.name} and his address is {dog2.owner.address} and his phone number is {dog2.owner.phone_number}')