class Animal(object):
     def __init__(self,sound,name,age,favorite_color):
        self.sound=sound
        self.name=name
        self.age=age
        self.favorite_color=favorite_color
     def eat(self,food):
     	print("yummy!!!!"+self.name+"is eating" +food)
     def description(self):
     	print(self.name+"is"+self.name+"years old and loves the color"+self.favorite_color)
     def make_sound (self):
     	print(self.sound)
mousa=Animal("roar"+"lion"+"2"+"pink")
