class stack:
    def __init__(self,m):
        self.max=m 
        self.l=[]
        self.top=-1
    def push(self):
        if self.top==self.max-1:
            print(">> Stack Overflow")
            return
        item=int(input("Enter Item:"))
        self.top+=1
        self.l.append(item)
        print(">> ",item,"Is Inserted to stack")
        print(self.l)
    def pop(self):
        if self.top==-1:
            print("Stack is Empty")
            return
        item=self.l.pop(self.top)
        self.top-=1
        print(">>",item,"Is Deleted From Stack")
        print(self.l)
m=int(input("Enter The Size of Stack: "))
obj=stack(m)
while True:
    print("<<**** STACK OPERATION****>>")
    print("\t\t1.Push")
    print("\t\t2.Pop")
    print("\t\t0.Exit")
    n=int(input("Enter Your Choice: "))
    if n==1:
        obj.push()
    if n==2:
        obj.pop()
    if n==0:
        break