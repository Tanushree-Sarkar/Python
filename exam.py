# def remdup(l):
#     i=0
#     while i<len(l):
#         j=i+1
#         while j<len(l):
#             if l[i]==l[j]:
#                 l.pop(j)
#             j=j+1
#         i=i+1
#     return l
# print(remdup([3,5,7,5,3,7,10]))



# n=int(input("Enter a four digit number: "))
# arr=[]
# while n>0:
#         rem = n % 10
#         arr.append(rem)
#         n = n // 10
# a=arr[0]
# arr[0]=arr[3]
# arr[3]=a
# k=0
# for i in range(4):
#     k=10*k+arr[i]
# print(k)

n=int(input("Enter limit: "))
a=0
b=1
count=3
i=2
if n==1:
    print(a)
else:
    print(a)
    print(2)
    print(b)
    while count!=n:
        print(2**i)
        count=count+1
        c=a+b
        a=b
        b=c
        print(c)
        i=i+1
        count=count+1
        if count==n:
            break
