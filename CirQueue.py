class CirQueue:
    def __init__(self,s):
        self.size=s
        self.front=-1
        self.rear=-1
        self.l=[0]*self.size
    def insert(self):
        if self.front==(self.rear+1)%self.size:
            print("Queue is Full")
            return
        self.rear=(self.rear+1)%self.size
        item=int(input("Enter item: "))
        self.l[self.rear]=item
        print(">>",item,"Is inserted to Queue")
        if self.front==-1:
            self.front=0
    def delete(self):
        if self.front==-1:
            print("Queue is empty")
            return
        item=self.l[self.front]
        print(item,"is deleted from Queue")
        if self.rear==self.front:
            self.rear=1
            self.front=-1
        else:
            self.front=(self.front+1)%self.size
    def display(self):
        if self.front==-1:
            print("Queue is empty")
            return
        if self.front<self.rear:
            print(self.l[self.front:self.rear+1])
        else:
            print(self.l[self.front:self.size+1] + self.l[:self.rear+1])
if __name__ == '__main__':
        s=int(input("Enter The Size of Queue: "))
        obj = CirQueue(s)
        while True:
            print("\n<<CIRCULAR QUEUE OPERATION >>")
            print("\t\t1.Insert ")
            print("\t\t2.Delete ")
            print("\t\t3.Traverse")
            print("\t\t0.Exit")
            n=int(input("Enter Your Choice: "))
            if n==1:
                obj.insert()
            if n == 2:
                obj.delete()
            if n == 3:
                obj.display()
            if n==0:
                break