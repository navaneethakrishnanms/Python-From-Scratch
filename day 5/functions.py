def word_count(string):
    words = string.split()
    return len(words)
def char_count(string):     
    char_count = len(string.replace(" ", ""))
    return char_count

 
   
a = input("Enter a sentence: ")
word_count(a)
print("Word count:", word_count(a))
print("Character count:", char_count(a))