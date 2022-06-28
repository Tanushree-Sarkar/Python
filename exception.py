# l=[1,2,3,4,5,6,7]
# try:
#     a=l[5]
#     print(a)
# except IndexError:
#     print('Exception caught')
# print('Example of exception')

# l=[1,2]
# a=l[5]
# print(a)
# print('Example of exception')

# a=20
# b=a/0
# print(b)

# a=20
# try:
#     b=a/0
#     print(b)
# except ZeroDivisionError:
#     print('Exception caught')

# try:
#     print('Programmer')
#     raise IndexError 
# except IndexError:
#         print('Exception caught')
# print('End of program')

class wrong(Exception):
    pass
try:
    print('Programmer')
    raise wrong
except wrong:
        print('Exception caught')
print('End of program')