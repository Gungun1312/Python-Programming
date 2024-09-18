def funct10(num):
        myproduct = lambda n : n*num
        return myproduct
    
var10 = funct10(10)
var20 = funct10(20)
print(var10(3))
print(var20(4))
print(funct10(30)(5))
print(type(var10))

