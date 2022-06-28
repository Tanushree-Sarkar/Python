class node:
    def __init__(self,item):
        self.info=item
        self.link=None
class linklist:
    def __init__(self):
        self.start=None
    def insert_at_last(self,item):
        n=node(item)
        if self.start==None:
            self.start=n
            print("Item INserted")
        else:
            t=self.start
            while t.link!=None:
                t=t.link
            t.link=n
            print("Item Inserted")
    def insert_at_beg(self,item):
        n=node(item)
        n.link=self.start
        self.start=n
    def delete_first(self):
        t=self.start
        if t==None:
            print("\nNo Element is Present")
        else:
            t=t.link
            self.start=t
            print("Deleted")
    def delete_last(self):
        t=self.start
        if t==None:
            print("Empty")
        elif t.link==None:
            self.start=None
        else:
            while t.link!=None:
                prev=t
                t=t.link
            prev.link=None
        print("Deleted")
    def traverse(self):
        t=self.start
        if t==None:
            print("List is Empty")
        else:
            while t!=None:
                print(t.info,end=',')
                t=t.link
    
if __name__ == '__main__':
        obj = linklist()
        while True:
            print("\n\t\t1.Insert at last ")
            print("\t\t2.Insert at beginning ")
            print("\t\t3.Traverse")
            print("\t\t4.Delete First")
            print("\t\t5.Delete Last")
            print("\t\t0.Exit")
            n=int(input("Enter Your Choice: "))
            if n==1:
                n1=int(input("Enter Your item: "))
                obj.insert_at_last(n1)
            if n == 2:
                n1=int(input("Enter Your item: "))
                obj.insert_at_beg(n1)
            if n == 3:
                obj.traverse()
            if n==4:
                obj.delete_first()
            if n==5:
                obj.delete_last()
            if n==0:
                break