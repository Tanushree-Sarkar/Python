# f1=open('Tanushree.py','w')
# # f1.write('Hi')
# # f1.writelines('Hello')
# # f1.writelines('World')
# # f1.close()
# f1=open('Tanushree.py','r')
# print(f1.readlines())
# f1.close()
f1=open('Tanushree.py','r')
print(f1.read())
f1.close()
f1=open('Tanushree.py','a')
f1.write('Hello')
f1.close()
f1=open('Tanushree.py','r')
print(f1.read())
f1.close()