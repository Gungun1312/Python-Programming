# how to detect wether a number is even or odd using bits.ConnectionAbortedError 
# if last bit is 0 then it is even and if it is 1 then it is odd.
num=100
result = "Odd" if (num&1) else "Even"
print(num,result)

num=105
result = "Odd" if (num&1) else "Even"
print(num,result)