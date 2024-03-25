a= input("Insert the word to analyse: ") 

for i, j in zip(a, reversed(a)): #the entire word is parsed, but is woudl be enough to parse the half word.
    if i != j:
        print("The Word", a, "is not a palindrome")
        break
else:
    print("The word", a, "is a palindrome" )