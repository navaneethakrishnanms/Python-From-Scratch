def name_recur(n,a):
    if a==0:
        return
    print(n)
    name_recur(n,a-1)
a=int(input("Enter the number:"))
n=input("Enter your name:")


name_recur(n,a)