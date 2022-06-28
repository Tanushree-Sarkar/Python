class array1:
    def __init__(self):
        self.l=[]
        self.max=int(input("Enter the size of the array: "))
    def CreateArray(self):
        print("Enter Value for the list: ")
        for i in range(self.max):
            t=int(input())
            self.l.append(t)
    def ShowArray(self):
        print(self.l)
    def LinearSearch(self,s):
        self.search=s
        flag=0
        for i in range(self.max):
            if self.l[i]==self.search:
                flag=1
                return i
        if flag==0:
            return False  
    def Sorting(self):
        self.l.sort()    
        print("Sorted Array:",self.l)   
        
    def binary_search(self,x):
        low = 0
        high =self.max
        mid = 0

        while low <= high:

            mid = (high + low) // 2

            # If x is greater, ignore left half
            if self.l[mid] < x:
                low = mid + 1

            # If x is smaller, ignore right half
            elif self.l[mid] > x:
                high = mid - 1

            # means x is present at mid
            else:
                return mid

        # If we reach here, then the element was not present
        return -1


# Function call
obj=array1()
obj.CreateArray()
obj.ShowArray()
s=int(input("Enter value for search: "))
t=obj.LinearSearch(s)
print("Element is present at index", t) 
obj.Sorting()
s1=int(input("Enter value for Binary search: "))
r=obj.binary_search(s1)
if r != -1:
    print("Element is present at index", r)
else:
    print("Element is not present in array") 