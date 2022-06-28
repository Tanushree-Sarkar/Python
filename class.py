# class student:
#     def given_data(self,r,n):
#         self.roll=r
#         self.name=n
#     def show_data(self):
#         print(self.roll)
#         print(self.name)
# s1=student()
# s1.given_data(1,'Tanushree')
# s1.show_data()
# s2=student()
# s2.given_data(2,'Gopal')
# s2.show_data()
#-----------------------------------------------------------------------------------------------------------
#-------HOMEWORK------

# class rectangle:
#     def getdata(self,l,b):
#         self.length=l
#         self.breadth=b
#     def printdata(self):
#         print("Length of the Rectangle is: ",self.length)
#         print("Breadth of the Rectangle is: ",self.breadth)
#     def area(self):
#         area=self.length*self.breadth
#         print("Area of the Rectangle is: ",area)
# r=rectangle()
# l=int(input("Enter Length for rectangle: "))
# b=int(input("Enter Breadth for rectangle: "))
# r.getdata(l,b)
# r.printdata()
# r.area()

# class student:
#     def __init__(self,r,n):
#         self.roll=r
#         self.name=n
#     def show_data(self):
#         print(self.roll)
#         print(self.name)
# s1=student('Gopal',1)
# s2=student('Avik',2)
# s1.show_data()
# s2.show_data()

# class student:
#     count=0
#     def __init__(self,r,n):
#         self.roll=r
#         self.name=n
#         student.count+=1
#     def show_data(self):
#         print(self.roll)
#         print(self.name)
#         print(student.count)
# s1=student('Gopal',1)
# s2=student('Avik',2)
# s1.show_data()
# s2.show_data()

# class student:
#     count=0
#     def __init__(self,n):
#         student.count+=1
#         self.roll=student.count
#         self.name=n
#     def show_data(self):
#         print("Roll: ",self.roll)
#         print("Name: ",self.name)
# s1=student('Gopal')
# s1.show_data()
# s2=student('Avik')
# s2.show_data()

# class student:
#     count=0
#     def __init__(self,n):
#         student.count+=1
#         self.roll=student.count
#         self.name=n
#     def __str__(self):
#        return('Name:{} Roll:{}'.format(self.name,self.roll))
# s1=student('Gopal')
# print(s1.__str__())
# s2=student('Avik')
# print(s2.__str__())

# class Student:
#     count=0
#     def __init__(self,n):
#         Student.count += 1
#         self.roll=Student.count
#         self.name=n
#     def __str__(self):
#         return(f"Name: {self.name} Roll: {self.roll}")
# obj=Student('Gopal')
# print(obj)
# obj2=Student('Avik')
# print(obj2)

# class student:
#     count=0
#     def __init__(self,n):
#         student.count+=1
#         self.roll=student.count
#         self.name=n
#     def __str__(self):
#        return('Name:{} Roll:{}'.format(self.name,self.roll))
#     def __del__(self):
#         print("Destructor Call")
# s1=student('Gopal')
# print(s1.__str__())
# s2=student('Avik')
# print(s2.__str__())
# s3=student('Tanushree')
# del s3
# print('Example of Destructor')
# print('Check it')

# class box:
#     def __init__(self,l,b,h):
#         self.length=l
#         self.breadth=b
#         self.height=h
#     def showdata(self):
#         print(self.length)
#         print(self.breadth)
#         print(self.height)
#     def volume(self):
#         v=self.length*self.breadth*self.height
#         print(v)
#     def __add__(self,B):
#         l=self.length+B.length
#         b=self.breadth+B.breadth
#         h=self.height+B.height
#         b=box(l,b,h)
#         return b
# b1=box(2,3,4)
# b2=box(1,1.2,3.2)
# b1.showdata()
# b1.volume()
# b3=b1+b2
# b3.showdata()
# b3.volume()

