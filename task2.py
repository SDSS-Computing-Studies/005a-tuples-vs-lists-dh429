#!python3

"""
Create a variable that contains an empy list.
Ask a user to enter 5 words.  Add the words into the list.
Print the list
inputs:
string 
string
string
string
string

outputs:
string

example:
Enter a word: apple
Enter a word: worm
Enter a word: dollar
Enter a word: shingle
Enter a word: virus

['apple', 'worm', 'dollar', 'shingle', 'virus']
"""
mylist = []

word1 = input("Enter a word:").strip
mylist.append(word1)
word2 = input("Enter a word:").strip
mylist.append(word2)
word3 = input("Enter a word:").strip
mylist.append(word3)
word4 = input("Enter a word:").strip
mylist.append(word4)
word5 = input("Enter a word:").strip
mylist.append(word5)


print(type(mylist))
print(mylist)