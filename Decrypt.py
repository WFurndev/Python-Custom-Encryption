import hashlib, base64
from decimal import *
#Paste directly
def factorial(num):
    n = 1
    i = 1
    while n < num:
        i += 1   
        n *= i
    return i
alphab=r" +/abcdVWXYZDEFGHIghOPQRSTUlmnopijkefABCJKLMNqrs=tuvwxyz1234567890"
val1=input().replace("\\", "")
print(val1+" \n is")
val2=int(input().replace("\\",""))
key2=factorial(int(input().replace("\\", "")))
key=input().replace("\\","")
for i in range(50):
	if str(hashlib.sha256(str(hashlib.sha256(str(i).encode()).hexdigest()).encode()).hexdigest())==key:
		key=int(Decimal(int(i)-7).sqrt())
		break
for i in range(key):
	val2=Decimal(val2).sqrt()
val2=val2.sqrt()-5
val2=val2.sqrt()
val1=val1.split("4824056")
do=""
for i in val1:
	i=Decimal(int(i)).sqrt()-key2
	i=Decimal(i)/Decimal(val2)**2
	do+=alphab[int(i)]
do = base64.b64decode(do.encode("ascii")).decode("ascii")
print("\n"+do)
exit()
