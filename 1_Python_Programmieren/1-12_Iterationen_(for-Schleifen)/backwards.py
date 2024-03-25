a= input("Insert the word: ")
b=""
for i in reversed(a):
    b = b+i
print(b)

#alternative with sclicing
# if a == a[::-1]:
#    print("The word", a , " is a palindrome")
#  else:
#    print("The word", a , " is NOT a palindrome")