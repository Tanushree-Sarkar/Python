# class MyDate:
#     def __init__(self):
#         self.d=int(input("Enter Date:"))
#         self.m=int(input("Enter Month:"))
#         self.y=int(input("Enter Year:"))
#     def addDays(self):
#         c=int(input("How many days you want to add:"))
#         date=self.d+c
#         mon=self.m
#         year=self.y
#         while date>31:
#             if mon in[1,3,5,7,8,10] and date>31:
#                 mon=mon+1
#                 date=date-31
#             if mon in[4,6,9,11] and date>30:
#                 mon=mon+1
#                 date=date-30
#             if mon in[2] and year%4==0 and date>29:
#                 mon=mon+1
#                 date=date-29
#             if mon in[2] and year%4!=0 and date>28:
#                 mon=mon+1
#                 date=date-28
#             if mon in[12] and date>31:
#                 date=date-31
#                 year=year+1
#                 mon=1
#         self.d=date
#         self.m=mon
#         self.y=year
#         print("New Date is:{}/{}/{}".format(self.d,self.m,self.y))

#     def addMonths(self):
#         c=int(input("How many months you want to add:"))
#         mon=self.m
#         year=self.y
#         date=self.d
#         date=date+(30*c)
#         while date>31:
#             if mon in[1,3,5,7,8,10] and date>31:
#                 mon=mon+1
#                 date=date-31
#             if mon in[4,6,9,11] and date>30:
#                 mon=mon+1
#                 date=date-30
#             if mon in[2] and year%4==0 and date>29:
#                 mon=mon+1
#                 date=date-29
#             if mon in[2] and year%4!=0 and date>28:
#                 mon=mon+1
#                 date=date-28
#             if mon in[12] and date>31:
#                 date=date-31
#                 year=year+1
#                 mon=1
#         self.d=date
#         self.m=mon
#         self.y=year
#         print("New Date is:{}/{}/{}".format(self.d,self.m,self.y))

#     def addYears(self):
#         c=int(input("How many Year you want to add:"))
#         mon=self.m
#         year=self.y+c
#         date=self.d
#         if mon in[2] and year%4!=0 and date==29:
#             date=28
#         self.d=date
#         self.m=mon
#         self.y=year
#         print("New Date is:{}/{}/{}".format(self.d,self.m,self.y))
# s1=MyDate()
# s1.addDays()
# s1.addMonths()
# s1.addYears()

# class student:
#     def __init__(self,n,r):
#         self.name=n
#         self.roll=r
#     def show(self):
#         print("Name: ",self.name)
#         print("Roll: ",self.__roll)
# s1=student('Tanushree',1)
# s1.show()
# print(s1.name)
# print(s1.__roll)

class A:
    def __init__(self,n):
        self.name=n
    def show(self):
        print('Name: ',self.name)
class B:
    def __init__(self,n,r):
        A.__init__(self,n)
        self.roll=r
  
class C(A,B):
    def __init__(self,n,r,c):
        A.__init__(self,n)
        B.__init__(self,n,r)
        self.course=c
    def display(self):
        print(self.name)
        print(self.roll)
        print(self.course)
obj=C('Tanushree',1,'MCA')
obj.display()
