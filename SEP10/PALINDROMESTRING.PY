a=input("Enter a string:")

rev=a[::-1]
print(rev)
if(a==rev):
    print("It is palindrome")
else:
    print("Not a palindrome")