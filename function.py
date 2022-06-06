def word(val):
    vowels=0
    consonants=0
    for x in range(len(val)):
        if val[x] in ['a','e','i','o','u']:
            vowels=vowels+1
        else:
            consonants=consonants+1
            
                
word()

# Exercise 4: Define a function that accepts a number and returns whether the number is even or odd.

import math


def number(num):
 if num%2==0:
     print("Even")
 else:
      print ("odd")  
 
number(10)

#  Define a function which counts vowels and consonant in a word.
def test(word):
    word=word.lower()
    vowel=0
    cons=0
    vowels=["a","e","i","o","u"]
    for x in word:
        if x in vowels:
            vowel+=1
        else:
            cons+=1 

test("Eoraa")

# Exercise 6: Define a function that returns Factorial of a number.
def factorial(x):
       return math.factorial(x)

print(factorial(5))

# Exercise 7: Define a function that accepts lowercase words and returns uppercase words.
   
from cmath import pi


def word(a):
    word=a.lower()

    print(word.upper())

word("HILDA")
# Exercise 8: Define a function that accepts radius and returns the area of a circle.

def radius(r):
    area=3.142*r*r
    return area
(10)




