
# Exercise 1: Write a program to reverse a string in python.

# import string


# def revers(a):
#     word=string(a.revese())
#     print("word")
# revers("python")
# Exercise 2: Write a program to count vowels and consonants in a string.
def count(a):
    vowels=0
    consonants=0
    word=a.lower()
    for x in range (len(a)):
        if a[x] in ['a','a','i','o','u']:
            vowels=vowels+1
        else:
            consonants=consonants+1
            print("total vowels are:",vowels)

            print("total consonants are ",consonants)
    
count("Hilda")


# Exercise 4: Write a program to count the number of letters in a word.
 

    




