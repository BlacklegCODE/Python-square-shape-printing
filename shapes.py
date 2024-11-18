import time

a = int(input("Enter number of columns :"))
b = int(input("Enter number of rows :"))
x = input("Enter any symbol :")
y = int(input("Enter duration each number takes to appear :")

for i in range(a):
  for ii in range(b):
    time.sleep(y)
    print(x,end = " ")
  print() # this print statement just adds a new line after each iteration
