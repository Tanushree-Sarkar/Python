# def main():
#     n=int(input("Enter any number: "))
#     f=0
#     for i in range(2,n,1):
#         if(n%i==0):
#             print("Not prime")
#             break
#         else:
#             f=1
#     if(f!=0):
#         print("prime")
# if __name__=='__main__':
#     main()

# def main():
#     n=int(input("Enter an integer: "))
#     for i in range(2,n+1):
#         if(n%i==0):
#             print(i)
# if __name__=='__main__':
#     main()

# def main():
#     n=int(input("Enter an integer: "))
#     while(n%2==0):
#         print(2)
#         n=n//2
#     for i in range(3,n):
#         while(n%i==0):
#             print(i)
#             n=n//i
#     if n>2:
#         print(n)
# if __name__=='__main__':
#     main()

# def test(n):
#     for i in range(2,n):
#         for j in range(i,n):
#             if n%i==0:
#                 r=i
#                 print(r)
#                 g=n//i
#                 n=g
#                 if n%i!=0 and n==i:
#                     print(n)
#     if n>2:
#         print(n)
# test(45)

# def prime(m):
#     count = 0
#     for i in range(2, m):
#         if (m % i == 0):
#             count = 1
#             break
#     if count == 0:
#         return m
# def main(n):
#     i=2
#     while i<n:
#         if prime(i):
#             if n%i==0:
#                 print(i)
#                 n=n/i
#     print(n)
# main(45)

# def sum():
#     n=int(input("Enter Terms: "))
#     fact=1
#     d=1
#     sum1=1
#     for i in range(1,n+1):
#         fact=fact*i
#         d=i/fact
#         sum1=sum1+d
#     print(sum1)
# sum()

# def sum():
#     n=int(input("Enter Terms: "))
#     d=1
#     sum1=1
#     for i in range(1,n+1):
#         d=i//i
#         sum1=sum1+d
#     print(sum1)
# sum()