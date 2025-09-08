def rev_recur(n):
    if n==0:
        return
    print(n)
    rev_recur(n-1)
a=int(input())
rev_recur(a)    