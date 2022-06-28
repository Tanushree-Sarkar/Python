n=int(input("Enter any number: "))
m=n*9
sum=0
print(m)
while sum!=9:
    sum=0
    while m!=0:
        sum=sum+m%10
        m=m//10
    m=sum
print("Yes the addition is ",sum)