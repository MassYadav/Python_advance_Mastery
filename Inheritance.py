# class FMumbai:
#     a = "I am an attribute of FMumbai class"
#     def hello(self):
#         print("i am a method of FMumbai class")

# class Fpune(FMumbai):
#     pass
# obj = FMumbai()

# obj2 = Fpune()
# print(obj2.a)
# obj2.hello()


# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def show(self):
#         print(f"the name is {self.name},{self.age}")

# class Dog(Animal):
#     def __init__(self,name,age):
#         super().__init__(name)
#         self.age = age
#     def show(self):
#         print(f"the name is {self.name}, {self.age} years old")    
# obj1 = Animal("timm")

# obj = Dog("timm",5)
# obj.show()
class Factory:
    def __init__(self,material,zips):
        self.material = material
        self.zips = zips

class PuneFactory:
    def __init__(self,material,zips,pockets):
        super().__init__(material,zips)
        self.pockets = pockets
class MumbaiFactory:
    def __init__(self,material,zips,pockets,colour):
        super().__init__(material,zips,pockets)
        self.colour = colour        

obj = PuneFactory("leather",2,4)
print(obj.material)
obj2 = MumbaiFactory("canvas",1,2,"red")
print(obj2.colour)