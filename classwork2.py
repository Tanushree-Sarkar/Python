# l=[1,2,'A',165]
# print(l)
# l.append('MCA')
# print(l)
# l.insert(3,36)
# print(l)
# l1=l[2:]
# print(l1)
# l1.append([9,8,6])
# print(l1)

# l=[1,2,3,4,5,6,7]
# l1=[]
# for i in range(0,len(l),1):
#     l2=l[0:i+1]
#     l1.append(l2)
# print(l1)
# add=0
# l=[10,20,30,40,50,60]
# l1=[]
# for i in range(1,len(l),1):
#     l2=l[0:i]
#     add=add+l2[i-1]
#     l1.append(add)
# print(l1)

l=[36,15,30,28,50,44,32,23]
for i in range(0,len(l)-1,1):
    if(l[i]<l[i+1]):
        f=l[i]
        l[i]=l[i+1]
        l[i+1]=f
        
print(l)