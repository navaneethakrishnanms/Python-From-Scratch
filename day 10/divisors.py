a=int(input())

print(f"Divisors of {a}:")
for i in range(1, a+1):
    if a % i == 0:
        print(i, end=" ")
