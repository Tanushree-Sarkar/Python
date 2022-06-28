#Calculate Factorial of 5
def fact():
    i=1
    fact=1
    while i<=5:
        fact=fact*i
        i=i+1
    return fact
show=fact()
print(show)

#Calculate Area of circle
def area():
    r=2.8
    p=22/7
    area=p*r*r
    return area
show=area()
print(show)

#Calculate Volume of a Sphere
def volume():
    r=3
    p=22/7
    v=4/3*p*(pow(r,3))
    return v
show=volume()
print(show)

#Check Prime number and Odd Even
n=int(input("Enter any number: "))
def prime():
    f=0
    for i in range(2,n,1):
        if(n%i==0):
            print("It is Not prime")
            break
        else:
            f=1
    if(f!=0):
        print("It is prime")
def check():
    if (n%2==0):
        print("It is Even Number")
    else:
       print("It is Odd Number") 
prime()
check()