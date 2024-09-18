

# ***********             (i,n,m)
# .*********            .=>(i-1) 
# ..*******             *=>(2*(m-1)+1)
# ...*****
# ....***
# .....*
# ....***
# ...*****                 .=>(n-i)
# ..*******                *=>(2*(i-m)+1)
# .*********
# ***********

while(True):
    n=int(input("please enter the number of layers"))
    if(n%2==1) : break
m= (n+1)//2
for i in range (1,n+1):
    if(i>m):b=(n-i); s=(2*(i-m)+1)
    else: b=(i-1); s = (2 * (m - i) + 1)
    print ("." * b + "*" * s)
print ("End of the program...")

