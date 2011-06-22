import math

productInt = math.factorial(100)
productString = str(productInt)

sum = 0

for i in range(len(productString)):
    sum += int(productString[i])

print sum


