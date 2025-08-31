a=int(input())
n=a
k=0
while a>0:
    b=a%10
    k=(k+(b**3))
    a=a//10
if(n==k):
    print("Amstrong")
else:
    print("Not amstrong")        