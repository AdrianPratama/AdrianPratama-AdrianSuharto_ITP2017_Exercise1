x = 2000
y = 3201
number = []
for i in range (x , y):
    if(i%7==0 and i%5 != 0):
        number.append(i)
    else:
        continue
print (number)
