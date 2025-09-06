def fact(n):
  if (n<=1):
    return n
  return n*fact(n-1)
a=int(input())
print(f'Factorial of {a} numbers: {fact(a)}')