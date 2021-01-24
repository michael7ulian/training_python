class person(object):
    def __init__(self,name,idnumber):
        self.name = name
        self.idnumber = idnumber
        
    def display(self):
        print(self.name)
        print(self.idnumber)

class employee(person):
    def __init__(self,name,idnumber, salary,post):
        self.salary = salary
        self.post = post
        
        person.__init__(self,name,idnumber)

    def display2(self):
        print(self.name)
        print(self.idnumber)
        print(self.salary)
        print(self.post)
        print(self.name)
        


        
a = employee('michael',20200,20087,"intern")
a.display()
print("="*100) 
a.display2()