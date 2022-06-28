class Item:
    def __init__(self):
        self.name=input("Enter Name Of Item: ")
        self.price=int(input("Enter Price: "))
        self.quantity=int(input("Enter the available quantity: "))
    def purchase(self):
        self.n=int(input("Enter the quantity parchase by customer: "))
        while self.n>self.quantity:
            print("Not availabe.....please try with less quantity ")
            self.n=int(input("Enter the quantity parchase by customer: "))
        else:
            self.m=self.quantity-self.n
            print("The available quantity is: ",self.m)
    def increasestock(self):
        self.s=int(input("Enter the quantity which arrived: "))
        self.st=self.s+self.m
        print("The available quantity is: ",self.st)
    def display(self):
        print("Item Name: ",self.name)
        print("Item price: ",self.price)
        print("Available Quantity: ",self.st)
ob=Item()
ob.purchase()
ob.increasestock()
ob.display()
