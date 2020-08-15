#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Write a program which will find factors of given number and find whether the factor is even or odd
num =int(input("enter the numbers : "))
for i in range(1,num+1):
    if (num%i==0):
        if(i%2==0):
            print("its a even number and the number is :" ,i)
        else:
            print("its a odd number and the number is :" , i)
print("***end***")


# In[ ]:


# Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically. 
str="hai these is a veeresh and iam student of edurekha"
string_split=str.split(" ")
print(string_split)
string_split.sort()
print(string_split)
for i in string_split:
    print(i)
print("***end***")


# In[ ]:


# Write a program, whichwill find all the numbers between 1000 and 3000 (both included) such that each digit of a number is an even number. The numbers obtained should be printed in a comma separated sequence on a single line.
items= []

for i in range(1000,3001):
    num1=str(i)
    if int(num1[0])%2==0 and int(num1[1])%2==0 and int(num1[2])%2==0:

        items.append(num1)

print(",".join(items))

print("****end****")


# In[ ]:


# Write a program that accepts a sentence and calculate the number of letters and digits.
num1=input("enter the string:")
digit=alpha=0
for i in num1:
    if(i.isdigit()):
        digit+=1
    elif(i.isalpha()):
        alpha+=1
    else:
        pass

print("the total characters are:",digit)
print("the total numbers are:",alpha)
print("****end****")


# In[ ]:


# Design a code which will find the given number is Palindrome number or not.
num1=input("enter the number:")
if(num1==num1[::-1]):
    print("the enterd string is a palindrome")
else:
    print("the enterd string is not palindrome")
print("****end****")

