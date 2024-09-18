class MyFirstClass :
    """This is a document string..."""
    class_var1 = 100 #class or static variable
    def __init__(self,data1):
        print ("Executing the constructor method...")
        self.int_var1 = data1 #instance variable
    def display (self):
        print("Executing display() method...")
        print (f"class varibale class_var1 = {MyFirstClass.class_var1} and {self.class_var1}...")
        print (f"instance variable inst_var1 = {self.int_var1}...")
    def update(self):
        print ("updating class or static variable..")
        MyFirstClass.class_var1 +=10
ob1 = MyFirstClass(111)
ob1.display()
print (ob1.__doc__)
print (MyFirstClass.__doc__)
ob1.update()
ob2 = MyFirstClass(222)
ob2.display()