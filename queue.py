class queue:
    def __init__(self,s):
        self.size=s
        self.rear=-1
        self.front=-1
        self.l=[0]*self.size
    def insert(self):
        if self.rear==self.size-1:
            print("Queue is full")
            return
        item=int(input("Enter Item:"))
        self.rear=self.rear+1
        self.l[self.rear]=item
        if self.front==-1:
            self.front=0
        print(">> ",item,"Is Inserted to Queue")
    def delete(self):
        if self.front==-1:
            print("Queue is empty")
            return
        item=self.l[self.front]
        print(">>",item,"Is Deleted From Queue")
        if self.front==self.rear:
            self.front=-1
            self.rear=-1
        else:
            self.front=self.front+1
    def display(self):
        if (self.front==-1):
            print("Queue is empty")
            return
        print(self.l[self.front:self.rear+1])
m=int(input("Enter The Size of Queue: "))
obj=queue(m)
while True:
    print("<<**** QUEUE OPERATION****>>")
    print("\t\t1.Insert")
    print("\t\t2.Delete")
    print("\t\t3.Display")
    print("\t\t0.Exit")
    n=int(input("Enter Your Choice: "))
    if n==1:
        obj.insert()
    if n==2:
        obj.delete()
    if n==3:
        obj.display()
    if n==0:
        break