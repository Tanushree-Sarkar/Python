# def star():
#     print("*")
#     print("**")
#     print("***")
# star()

# def sum():
#     a=10
#     b=20
#     c=a+b
#     return c
# s=sum()
# print(s)

# def fact():
#     i=1
#     fact=1
#     while i<=5:
#         fact=fact*i
#         i=i+1
#     return fact
# show=fact()
# print(show)

# def area():
#     r=2.8
#     p=22/7
#     area=p*r*r
#     return area
# show=area()
# print(show)

# def volume():
#     r=3
#     p=22/7
#     v=4/3*p*(pow(r,3))
#     return v
# show=volume()
# print(show)

# n=int(input("Enter any number: "))
# def prime():
#     f=0
#     for i in range(2,n,1):
#         if(n%i==0):
#             print("It is Not prime")
#             break
#         else:
#             f=1
#     if(f!=0):
#         print("It is prime")
# def check():
#     if (n%2==0):
#         print("It is Even Number")
#     else:
#        print("It is Odd Number") 

# prime()
# check()

# p=pow(3,3)
# print(p)

# def fun(a,b):
#     s1=a+b
#     s2=a-b
#     s3=a*b
#     return s1,s2,s3
# sum,sub,mul=fun(10,20)
# print(sum)
# print(sub)
# print(mul)
# fun.author='Tanushree'
# fun.date='4th Jan'
# show=fun
# print(fun.author)
# print(show.date)

# def fun1():
#     print('Hi')
#     def fun2():
#         print('Students')
#     fun2()
# print('Nested Function')
# fun1()

print('Hi Students')
print(repr(__name__))