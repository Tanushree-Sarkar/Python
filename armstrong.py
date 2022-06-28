# class Armstrong:
#     def getLength(self,n):
#         self.c=n
#         self.count=0
#         while self.c!=0:
#             self.c=self.c//10
#             self.count=self.count+1
#         print(self.count)
#     def backup(self,b):
#         self.f=b
#         self.t=b
#     def checkArm(self):
#         self.sum=0
#         while self.f!=0:
#             self.rem=self.f%10
#             self.p=self.rem**self.count
#             self.sum=self.sum+self.p
#             self.f=self.f//10
#         if self.t==self.sum:
#             print("True")
#         else:
#             print("False")       
# n=int(input("Enter any number:"))
# obj=Armstrong()
# obj.getLength(n)
# obj.backup(n)
# obj.checkArm()

# class prime:
#     def __init__(self,n):
#         self.n1=n
#     def primecheck(self):
#         f=0
#         for i in range(2,self.n1//2,1):
#             if(self.n1%i==0):
#                 print("Not prime")
#                 break
#             else:
#                 f=1
#         if(f!=0):
#             print("prime")
# if __name__=='__main__':
#     n=int(input("Enter any number: "))
#     obj=prime(n)
#     obj.primecheck()
