class post:
    def __init__(self,m,n):
        self.max=m 
        self.s=n
        self.s=self.s.split(",")
        self.l=[]
        print(self.s)
    def process(self):
        for i in range(self.max):
            if self.s[i].isdigit():
                self.l.append(int(self.s[i]))
            elif self.s[i]=="+":
                a=self.l.pop()
                b=self.l.pop()
                self.l.append(int(a)+int(b))
            elif self.s[i]=="*":
                a=self.l.pop()
                b=self.l.pop()
                self.l.append(int(a)*int(b))
            elif self.s[i]=="/":
                a=self.l.pop()
                b=self.l.pop()
                self.l.append(int(b)//int(a))
            elif self.s[i]=="-":
                a=self.l.pop()
                b=self.l.pop()
                self.l.append(int(b)-int(a))
        print(self.l)
m=int(input("Enter The Size of Stack: "))
n=input("Enter input: ")
obj=post(m,n) 
obj.process()