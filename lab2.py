# def fun():
#     n=int(input("Enter terms: "))
#     for i in range(1,n,2):
#         print(i," ",end="")
# fun()

# def check():
#     n=int(input("Enter any number: "))
#     if (n%2!=0):
#          print("It is Odd Number") 
#     else:
#         print("It is not Odd Number") 
# check()


# def large(n1,n2,n3):
#     if (n1 >= n2) & (n1 >= n3):
#         l=n1
#     elif (n2 >= n1) & (n2 >= n3):
#         l=n2
#     else:
#         l=n3
#     return l
# n1=int(input("Enter 1st Number: "))
# n2=int(input("Enter 2nd Number: "))
# n3=int(input("Enter 3rd Number: "))
# l=large(n1,n2,n3)
# print("Largest Number is :",l)

# n=int(input("Enter any number: "))
# def fact():
#     i=1
#     fact=1
#     while i<=n:
#         fact=fact*i
#         i=i+1
#     return fact
# show=fact()
# print(show)

# def func(rows):
#     for i in range(1,rows+1):
#         for j in range(1,rows+1):
#             print(i," ",end="")
#         print()
# rows=int(input("Enter number: "))
# func(rows)

# def rev():
#     n=int(input("Enter any digit number: "))
#     reverse=0
#     while n!=0:
#         rem=n%10
#         reverse=reverse*10+rem
#         n=n//10
#     print(reverse)
# rev()

def fibo(n):
    i = 0
    j = 1
    sum = 0
    count = 1
    while (count <= n):
        print(sum, end=" ")
        count =count+1
        i = j
        j= sum
        sum = i + j
def main():
    n=int(input("Enter any number: "))
    fibo(n)
main()

  
def fibo(n):
    n1=0
    n2=1
    print(n1,end=" ")
    for i in range(1,n):
        print(n2,end=" ")
        sum=n1+n2
        n1=n2
        n2=sum
def main():
    n=int(input("Enter any number: "))
    fibo(n)
if __name__=='__main__':
    main()

# def compare(n):
#  f=(9*n+160)/5
#  print(n==f)
# def main():
#  n=int(input("Enter Temperature: "))
#  compare(n)
# if __name__=="__main__":
#  main()
