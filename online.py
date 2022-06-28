#Challenge
# Capital indexes
# Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.

# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
def capital_indexes(s):
    t=[]
    
    for i in range(len(s)):
        if s[i]>='A' and s[i]<='Z':
            t.append(i)
    return t
n='HeLlO'
print(capital_indexes(n))

# Challenge
# Middle letter
# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

# For example, mid("abc") should return "b" and mid("aaaa") should return "".

def mid(s):
    l=len(s)
    if l%2==0:
        return " "
    else:
        d=l//2
        return s[d]
n="abc"
print(mid(n))

# Challenge
# Online status
# The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

# For example, consider the following dictionary:

# statuses = {
#     "Alice": "online",
#     "Bob": "offline",
#     "Eve": "online",
# }
# In this case, the number of people online is 2.

# Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.

# Your function should return the number of people who are online.

def online_count(d):
    c=0
    for i in d:
        if d[i]=='online':
            c=c+1
    return c
d1={
    'Sakshi':'online',
    'Tanushree':'offline',
    'Gopal':'online'
}
print(online_count(d1))