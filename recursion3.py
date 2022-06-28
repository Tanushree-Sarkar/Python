# def reverse(n,l):
#     if n>0:
#         rem = n % 10
#         if(rem not in l):
#             l.append(rem)
#         n = n // 10
#         reverse(n,l)
#     return l
# l = []
# n=int(input("Enter Any Number: "))
# print(reverse(n,l))

# # Input an integer and print each digit
# def reverse(n):
#     if n>0:
#         rem = n % 10
#         n = n // 10
#         reverse(n)
#         print(rem)
# n=int(input("Enter Any Number: "))
# reverse(n)

# # Reverse integer and print each digit
def reverse(n):
    if n>0:
        rem = n % 10
        print(rem,end="")
        n = n // 10
        reverse(n)
n=int(input("Enter Any Number: "))
reverse(n)

#GCD Using Recursion
# def gcd(a, b):
#     if (b == 0):
#         return a
#     else:
#         if a>b:
#             return gcd(b, a % b)
#         elif b>a:
#             return gcd(a, b % a)
# a =int(input("Enter 1st Number:"))
# b =int(input("Enter 2nd Number: "))
# print("GCD of {} and {} is:".format(a,b),gcd(a, b))

# #Factorial of a natural number using recursion
# f=1
# def fact(n):
#     global f
#     f=f*n
#     n=n-1
#     if n>0:
#         fact(n)
#     return f
# n=int(input("Enter Any Number: "))
# print("Factorial of {} is:".format(n),fact(n))

# Nth Position of  Fibonacci Series
# a = 0
# b = 1
# sum = 0
# count = 1
# def fibo(n):
#     global a,b,sum,count
#     if count <= n:
#         count =count+1
#         a = b
#         b = sum
#         sum = a + b
#         fibo(n)
#     return sum
# n=int(input("Enter The Position: "))
# print("{}th Number Fibonacci Series is: ".format(n),fibo(n))

# Multiplication Using Recursion without * sign
# c=0
# def multi(a,b):
#     global c
#     c=c+a
#     b=b-1
#     if b>0:
#         multi(a,b)
#     return c
# a=6
# b=7
# print(multi(a,b))

#::::a+a+a+a .... (a=a,b=n)::::
# def multiplies(a,b):
#   if a == 0 or b == 0:
#     return 0
#   else:
#     while b > 0:
#       b -= 1
#       return a + multiplies(a,b)
#
# a,b = map(int,input("Enter the value of a and b: ").split())
# print(multiplies(a,b))

# Input - 1126234   Output - [4, 3, 2, 6, 1]
# list = []
# def rev(n):
#   global list
#   if n>0:
#     rem = n % 10
#     if rem not in list:
#       list.append(rem)
#     rev(n//10)
#     return list
# print(rev(1126234))