# r=int(input("Enter value for rows: "))
# c=int(input("Enter value for columns: "))
# x=[]
# val=[]
# for i in range(r):
#     for j in range(c):
#         val.insert(j,(int(input("Enter value for [{}][{}]: ".format(i,j)))))
#     x.insert(i,val)
#     val=[]
# y=[]
# for i in range(r):
#     for j in range(c):
#         val.insert(j,(int(input("Enter value for [{}][{}]: ".format(i,j)))))
#     y.insert(i,val)
#     val=[]
# sum=[]
# for i in range(r):
#     for j in range(c):
#         val.insert(j,x[i][j]+y[i][j])
#     sum.insert(i,val)
#     val=[]
# print(sum)

# r=int(input("Enter value for rows: "))
# c=int(input("Enter value for columns: "))
# x=[]
# val=[]
# for i in range(r):
#     for j in range(c):
#         val[j]=int(input("Enter value for [{}][{}]: ".format(i,j)))
#     x[i]=val
#     val=[]
# y=[]
# for i in range(r):
#     for j in range(c):
#         val[j]=int(input("Enter value for [{}][{}]: ".format(i,j)))
#     y[i]=(val)
#     val=[]
# sum=[]
# for i in range(r):
#     for j in range(c):
#         val[j]=x[i][j]+y[i][j]
#     sum[i]=(val)
#     val=[]
# print(sum)

r=int(input("Enter value for rows: "))
c=int(input("Enter value for columns: "))
x=[]
val=[]
for i in range(r):
    for j in range(c):
        val.insert(j,(int(input("Enter value for [{}][{}]: ".format(i,j)))))
    x.insert(i,val)
    val=[]
y=[]
for i in range(r):
    for j in range(c):
        val.insert(j,(int(input("Enter value for [{}][{}]: ".format(i,j)))))
    y.insert(i,val)
    val=[]
sum=[]
print(y)
