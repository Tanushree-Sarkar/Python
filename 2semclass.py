# n=input("Enter a strng: ")
# for i in range(5):
#     print(n[i],end="")

# def repeat(str1):
#     dict = {}
#     for i in str1:
#         if i.islower()==True:
#             keys = dict.keys()
#             if i in('a','e','i','o','u'):
#                 if i in keys:
#                     dict[i] += 1
#                 else:
#                     dict[i] = 1
#     return dict
# print(repeat('institute'))

# n=int(input("Enter the limit: "))
# sum=0
# for i in range(n+1):
#     sum=sum+i
# print(sum)

# def small(n):
#     n.sort()
#     return n[2]
# n=[34,89,54,20,50,76,10,45,90]
# print(small(n))

str='aneeta'
print(str[0],end='')
for i in range(1,len(str)):
    if str[i-1]==str[i]:
        print("*",end='')
    else:
        print(str[i],end='')

# str='00011100000111'
# count=0
# l=[]
# for i in range(1,len(str)):
#     if str[i-1]==str[i]:
#         count=count+1
#     else:
#         l.append(count)
#         count=0
# print(l)
# print(max(l)+1)
