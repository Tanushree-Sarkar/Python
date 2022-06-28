import random
nump=random.randint(1000,9999)
n=int(input("Enter a 4 digit number: "))
while n!=10:
    num=nump
    cor=0
    while num%10:
        numc=num%10
        nc=n%10
        num=num//10
        n=n//10
        if numc==nc:
            cor=cor+1
    if cor==4:
        print("Congrats! you guessed it right")
        break
    else:
        print("{} digit were guessed right" .format(cor))
        n=int(input("Enter a 4 digit number: "))
print("You quit the game")