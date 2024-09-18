class Myclass:
    count_object = 0
    def __init__(self):
        Myclass.count_object +=1

ob1 = Myclass()
ob2 = Myclass()
ob3 = Myclass()
ob4 = Myclass()
print (f"Number of objects defined is {Myclass}") 