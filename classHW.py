class MyDate:
    d=int(input("Enter Date:"))
    m=int(input("Enter Month:"))
    y=int(input("Enter Year:"))
    def addDays(self):
        c=int(input("How many days you want to add:"))
        self.date=MyDate.d+c
        if MyDate.m in[1,3,5,7,8,10] and self.date>31:
            self.mon=MyDate.m+1
            self.date=MyDate.d-31
        elif MyDate.m in[4,6,9,11] and self.date>30:
            self.mon=MyDate.m+1
            self.date=MyDate.d-30
        elif MyDate.m in[2] and MyDate.y%4==0 and self.date>29:
            self.mon=MyDate.m+1
            self.date=MyDate.d-29
        elif MyDate.m in[2] and MyDate.y%4!=0 and self.date>28:
            self.mon=MyDate.m+1
            self.date=MyDate.d-28
        elif MyDate.m in[12] and self.date>31:
            self.year=1
        print("New Date is:{}/{}/{}".format(self.date,self.mon,self.year))
s1=MyDate()
s1.addDays()
    
