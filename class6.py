n=int(input("Enter any digit number: "))
reverse=0
while n!=0:
    rem=n%10
    reverse=reverse*10+rem
    n=n//10
print(reverse)

# n=int(input("enter no: "))
# d=n//100
# r=n%100
# print(r)


