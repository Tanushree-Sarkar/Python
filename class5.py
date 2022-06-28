p=0
negative=0
z=0
n=int(input("Enter terms: "))
for i in range(1,n+1,1):
    t=int(input("Enter No: "))
    if(t==0):
        z=z+1
    elif(t>0):
        p=p+1
    elif(t<0):
        negative=negative+1
print("Total Positive",p)
print("Total Negative",negative)
print("Total Zero",z)
    
