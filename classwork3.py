# d1={
#     4:'Avipsa',
#     3:'Soumyo',
#     1:'Tanu',
#     2:'Asmita',
#     5:'Gopal'
# }
# l=sorted(d1)
# for i in l:
#     print(d1[i])

d1={
    4:'Avipsa',
    3:'Soumyo',
    1:'Tanu',
    2:'Asmita',
    5:'Gopal'
}
for i in d1:
    print(list(d1[i]))


n=input("Enter your string: ")
n.replace(',','')
print(n.split())