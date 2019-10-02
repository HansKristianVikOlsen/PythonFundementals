import math
from math import factorial as fac
print(math.sqrt(81))
n = 5
k = 3
print(fac(n) // (fac(k) * fac(n-k)))

# if
if n > 5:
    print("aaa")
elif n == 5:
    print("bbb")
else:
    print("ccc")

while n > 0:
    print(n)
    n -= 13

# En kommentar

"""
while True:
    print("write number")
    response = input()
    if int(response) == 3:
        break
    else:
        print("not correct")
"""
# strings
c = 'oslo bååå'
print(c.capitalize())

testArray = []
testArray.append("A")
testArray.append("B")
testArray.append(2)
print(testArray)
print(testArray[1])

# dicionary
hoyde = {'hans': '180cm', 'miriam': '167cm'}

print(hoyde["miriam"])


# for loop
byer = ["Stavanger", "Oslo", "Bergen"]

for by in byer:
    print(by)

for key in hoyde:
    print(key, hoyde[key])
