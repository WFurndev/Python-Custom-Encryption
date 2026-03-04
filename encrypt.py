import random, hashlib, secrets, base64
print("Enter something to encrypt: ", end='')
inpu = input()
inpu=base64.b64encode(inpu.encode("ascii")).decode("ascii")
#inpu=base64.b64encode(inpu.encode("ascii"))
key=random.randint(1, 5)
alphab=r" +/abcdVWXYZDEFGHIghOPQRSTUlmnopijkefABCJKLMNqrs=tuvwxyz1234567890"
ext=random.randint(1, 3000)
key2 = random.randint(10,200)
def factorial(num):
    ret=1
    for i in range(int(num)-1):
        ret*=(i+1)
    return ret
def getPos(vals, fromin):
	number=0
	while number<len(fromin):
		if fromin[number]==vals:
			return ((number*(ext**2))+key2)**2
		number+=1
	return 0
val=[]
for i in inpu:
	val+=[str(getPos(i, alphab))]
val="4824056".join(val)
print(val)
ext=((ext**2)+5)**2
for i in range(key):
	ext=ext**2
key2=factorial(key2)


print(str(ext))
print(str(key2))
print(str(hashlib.sha256(str(hashlib.sha256(str(key**2+7).encode()).hexdigest()).encode()).hexdigest()))
exit()
