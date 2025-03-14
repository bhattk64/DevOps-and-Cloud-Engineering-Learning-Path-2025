class myclass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=myclass("Kul",25)
print(p1.name)
print(p1.age)
#1.Note:The _init_()function is called automatically every time the class is being used to create a new object

#2. The __str__() function controls what should be returned when the class object is represented as a string.
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return f"{self.name}({self.age})"
# p1=person("Kul",25)
# print(p1)


#3.objects=it can also contain methods.methods in object are function that belong to the object
class animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("Hello my name is:"+self.name)
p1=animal("Kul",20)
p1.myfunc()


# 4. python inheritance :parent class(it is the class being inherited from and also called base class),child class(it is the class that inherits from another class and also called derived class)
class parent:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
        x=parent("kul","chandra")
        x.printname()


#uuse the super()function-after using this you dont have to use the name of parent element it will automatically inherit the method and properties of its parent

class student(parent):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

#python iterators 
class myNumber():
    def __iter__(self):
        self.a=1
        return self 
    def __next__(self):
        x=self.a
        self.a+=1
        return x
myclass=myNumber()
myiter=iter(myclass)
print(next(myiter))
print(next(myiter))

#python polymorphism
class animal:
    def sound(self):
        print("Animal makes a sound")
class dog(animal):
    def sound(self):
        print("Dog barks")
        class cat(animal):
            def sound(self):
                print("Cat meows")
                d=dog()
                d.sound()
                c=cat()
                c.sound()
               

