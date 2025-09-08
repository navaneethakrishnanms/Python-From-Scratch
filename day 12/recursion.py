def num_recursion(n):
    if n==0:
        return
    num_recursion(n-1)
    print(n)


a=int(input())
num_recursion(a)