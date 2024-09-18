
factorial_cal =  lambda num : 1 if( num==0 or num==1) else num * factorial_cal(num-1)
print(type(factorial_cal))
print(factorial_cal(5))
print(factorial_cal(10))