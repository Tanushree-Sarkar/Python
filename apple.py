lst=[9,2,2,8,4,5]
sum1=sum(lst)
boy=len(lst)
sh = sum1//boy
count=0
if sum1%boy==0:
    print("Apple Amout Matched")
    ind = boy-1
    while ind>=0:
        if ind==boy-1:
            rind=0
        else:
            rind=ind+1

        if ind==0:
            lind=boy-1
        else:
            lind=ind-1
        while lst[rind]< sh and lst[ind]>sh:
            lst[rind]=lst[rind]+1
            lst[ind]=lst[ind]-1
            count=count+1
            print(lst)
        while (lst[ind]>sh):
            lst[lind]=lst[lind]+1
            lst[ind]=lst[ind]-1
            count=count+1
            print(lst)
        while (lst[ind]<sh and lst[lind]>0):
            lst[ind]=lst[ind]+1
            lst[lind]=lst[lind]-1
            count=count+1
            print(lst)
        ind=ind-1
print(count)

