class student:
    def __init__(self):
        self.rollNum=int(input("Enter roll number: "))
        self.name=input("Enter Name: ")
        self.marklist=[]
        self.stream=input("Enter Stream: ")
    def setMarks(self):
        for i in range(5):
            t=int(input("Enter marks for subject {} : ".format(i+1)))
            self.marklist.append(t)
    def getstream(self):
        if self.stream=='A':
            print('Stream is Arts')
        if self.stream=='C':
            print('Stream is Commerce')
        if self.stream=='S':
            print('Stream is Science')
    def percentage(self):
        self.total=sum(self.marklist)
        self.p=self.total//5
        print("Percentage is : ",self.p)
    def gradeGen(self):
        for i in self.marklist:
            if i>=90:
                print('Subject 1 Grade : A ')
            elif i<90 and i>=80:
                print('Subject 1 Grade : B ')
            elif i<80 and i>=65:
                print('Subject 1 Grade : C ')
            elif i<65 and i>=40:
                print('Subject 1 Grade : D ')
            elif i<40:
                print('E')
ob=student()
ob.setMarks()
ob.getstream()
ob.percentage()
ob.gradeGen()
        
