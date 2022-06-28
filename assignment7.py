# n=input("Enter your string: ")
# n.replace(',','')
# print(len(n.split()))

# nums = ['1','2','3','4','5','6','7','8','9','0', ',']
# n=input("Enter the amount of iteams: ")

# for i in n:
#     if n[i] in nums:
#         pass
#     else:
#         print("Enter digits only seperated by comma")

# t=0
# for i in range(n):
#     c=int(input("Enter the quantity: "))
#     p=int(input("Enter the price: "))
#     z=c*p
#     t=t+z
# print(t)

# class rectangle:
#     def __init__(self,l,b):
#         self.length=l
#         self.breadth=b
#     def setlength(self):
#         self.length=int(input("Enter New length: "))
#     def setbreadth(self):
#         self.breadth=int(input("Enter New breadth: "))
#     def getbreadth(self):
#         print("New breadth is",self.breadth)
#     def area(self):
#         area=self.length*self.breadth
#         print("Area of the Rectangle is: ",area)
#     def perimeter(self):
#         p=2*(self.length+self.breadth)
#         print("Perimeter of the Rectangle is: ",p)
    

# l=int(input("Enter Length for rectangle: "))
# b=int(input("Enter Breadth for rectangle: "))
# r=rectangle(l,b)
# r.setlength()
# r.setbreadth()
# r.getbreadth()
# r.area()
# r.perimeter()

n=input("Enter your string: ")
c=0
t=0
for i in n:
    if i==' ' or i==',':
        if c!=0:
            t=t+1
            c=0
    else:
        c=c+1
if c!=0:
    t=t+1
print(t)

# n=int(input("Enter the amount of iteams: "))
# t=0
# for i in range(1,len(n)):    
#     z=n[i]*n[i+1]
#     t=t+z
#     i=i+2
# print(t)


