# Bitwise Operators: & | ~ ^
# A => 65 => 64 + 1      => 0100 0001
#                        or 0010 0000 (32) 0x20
#                           ---------
# a => 97 => 64 + 32 + 1 => 0110 0001
mychar = 'A'
print (mychar)
mychar = chr(ord(mychar) | 32)
print (mychar)

mychar = 'A'
print (mychar)
mychar = chr(ord(mychar) | 0x20)
print (mychar)