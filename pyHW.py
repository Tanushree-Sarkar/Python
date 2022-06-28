# def reverse(n):
#     l=len(n)-1
#     while l>=0:
#         print(n[l])
#         l=l-1
# n=input("Enter Your String: ")
# reverse(n)

# def StrRev(n):
#     for i in range(len(n)-1,-1,-1):
#         print(n[i],end='')
# n=input("Enter Any String: ")
# StrRev(n)

# def fibo(n):
#     i = 0
#     j = 1
#     sum = 0
#     l=[]
#     while (sum <= n):
#         l.append(sum)
#         i = j
#         j= sum
#         sum = i + j
#     print(l[::-1 ])
# def main():
#     n=int(input("Enter any number: "))
#     fibo(n)
# main()

# def vowelcount(n):
#     count=0
#     for i in n:
#         if i in['a','i','e','o','u']:
#             count=count+1
#     return count
# n=input("Enter Your String: ")
# c=vowelcount(n)
# print(c)

# def largest(x,y,z):
#     if(x>y and x>z):
#         return x
#     if(y>x and y>z):
#         return y
#     if(z>x and z>y):
#         return z
# x=int(input("Enter 1st number: "))
# y=int(input("Enter 1st number: "))
# z=int(input("Enter 1st number: "))
# l=largest(x,y,z)
# print("Largest value is ",l)

 
# def func1():
#     a=10
#     b=20
#     print("This is Outer Function")
#     print("First value is ",a)
#     print("First value is ",b)
#     def func2():
#         c=a*b
#         s=a+b
#         print("This is inner Function")
#         print("Multiplication is ",c)
#         print("Addition is ",s)
#     func2()
# func1()
