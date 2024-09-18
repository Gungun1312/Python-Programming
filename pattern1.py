n = int(input("Please enter the number of layers:"))
for i in range(1, n + 1):
    print ("." * (n - i) + "*" * (2 * i - 1))
print ("End of the program...")


#  .....*
#  ....***                  (i,n)
#  ...*****                 (n-i) 
#  ..*******               (2*i-1)
#  .*********
#  ***********
#   i . *  
#   1 0 11           
#   2 1  9        
#   3 2  7
#   4 3  5
#   5 4  3
#   6 5  1

n = int(input("Please enter the number of layers:"))
for i in range(1, n + 1):
    print ("." * (i-1) + "*" * (2-(n-i)+1))
print ("End of the program...")




#        upside down                (  . => i-1)
#                            (  * => (2-(n-i)+1))


