# A program to count total zeros and ones in a binary number.
x=int(input('enter the number :'))
y=(bin(x))
print(y)
y=list((y[2:]))
print(y)
print("The Number of zeroes in binary number is :",y.count('0'))
print("The Number of one's in binary number is :",y.count('1'))



