# lst=[1,1,1,1,2,3,3,4,5,6,6,8,10,12]
# i=0
# while i<len(lst)-1:
#     while(lst[i]==lst[i+1]):
#         lst.remove(lst[i+1])
#     i=i+1
# print(lst)

lst=[1,3,4,1,6,10,2,3,8,6,2,12,4,4,4]
i=0
while i<len(lst)-1:
    j=i+1
    while j<len(lst):
        if(lst[i]==lst[j]):
            lst.pop(j)
        j=j+1
    i=i+1
print(lst)
