a=int(input())
f=0
if(a==1):
    print(f"{a} is Prime number")
for i in range(2,a):
    if(a%i==0):
        f=1
if(f==0):
    print(f"{a} is Prime number")
else:
    print(f"{a} is not a Prime number")