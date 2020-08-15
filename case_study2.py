#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# What is the output of the following code?
# nums = set([1,1,2,3,3,3,4,4])
# print(len(nums))
# Hint: Set consists unique element.

4


# In[ ]:


# What will be the output?
# d = {"john":40, "peter":45}
# print(list(d.keys()))
# Hint: d.keys() is the function which will show keys.

['john', 'peter']


# In[3]:


# A website requires a user to input username and password to register. Write a program
# to check the validity of password given by user. Following are the criteria for checking
# password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
passwd=input("enter th passpword:")

SpecialSym=['$','@','#']
return_val=True
return_val1=0
if (6<=len(passwd)<=12):
        return_val1=1
else:
    print("the length of password should be not be greater than 12 and lesser than 6")
 
if(return_val1==1):
    if not any(char.isdigit() for char in passwd):
        print('the password should have at least one numeral')
        return_val=False
    if not any(char.isupper() for char in passwd):
        print('the password should have at least one uppercase letter')
        return_val=False
    if not any(char.islower() for char in passwd):
        print('the password should have at least one lowercase letter')
        return_val=False
    if not any(char in SpecialSym for char in passwd):
        print('the password should have at least one of the symbols $@#')
        return_val=False

if return_val==True:
    print('OK')
else:
    print("NOT OK")
    
    
print("****end****")


# In[4]:


# Write a for loop that prints all elements of a list and their position in the list.
#  a = [4,7,3,2,5,9]
# Hint: Use Loop to iterate through list elements.
a = [4,7,3,2,5,9]

for i in a:
    print("Element:",i,"---->","index",a.index(i))


# In[6]:


# Please write a program which accepts a string from console and print the
# characters that have even indexes.
#  Example: If the following string is given as input to the program:
#  H1e2l3l4o5w6o7r8l9d
#  Then, the output of the program should be:
#  Helloworld

str1=input("enter the name:")
str_out=""
for i in str1:
    if(str1.index(i)%2==0):
      str_out+=i
print(str_out)
print("****end***")


# In[7]:


# Please write a program which accepts a string from console and print it in reverse
# order.
#  Example: If the following string is given as input to the program:
#  rise to vote sir
#  Then, the output of the program should be:
#  ris etov ot esir

str1=input("enter the name:")
print(str1[::-1])
print("***end***")


# In[8]:


# Please write a program which count and print the numbers of each character in a
# string input by console.
#  Example: If the following string is given as input to the program:
#  abcdefgabc
#  Then, the output of the program should be:

string = "veeresh is a student of edurekha "
lst1 = []
for char in string:
     if char not in lst1:
        lst1.append(char)
for item in lst1:
     print(item,"-->",string.count(item))
print("***end***")


# In[9]:


# With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a
# program to make a list whose elements are intersection of the above given lists.

set1=[1,3,6,78,35,55]
set2=[12,24,35,24,88,120,155]

def intersection(set1, set2):
    return(set(set1)&set(set2))

set_out=intersection(set1, set2)
print(list(set_out))
print("***end***")


# In[11]:


# By using list comprehension, please write a program to print the list after removing
# the value 24 in [12,24,35,24,88,120,155].

num1=24
list1 = [12, 24, 35, 24, 88, 120, 155]
print("Before -->",list1)
list2=list1.count(num1)
while(list2>0):
    list1.remove(num1)
    list2-=1
print("After -->",list1)
print("***end***")

list1 = [12, 24, 35, 24, 88, 120, 155]
list2 = [value for index,value in enumerate(list1) if value !=120 ]
print(list2)
print("***end***")


# In[13]:


# By using list comprehension, please write a program to print the list after removing
# the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

list1 = [12,24,35,70,88,120,155]
list2 = [value for index,value in enumerate(list1) if index not in (0,4,5) ]
print(list2)
print("***end***")


# In[14]:


# By using list comprehension, please write a program to print the list after removing
# delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

list1 = [24,35,70,88,120,155,7777]


list3= [value for index,value in enumerate(list1) if (value%5!=0 and value%7!=0) ]

print(list3)
print("***end***")


# In[15]:


# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by
# console (n>0).


num = int(input("Enter a number: "))
newnum = 0

for each in range(1,num+1):
    newnum = newnum+(each/(each+1))

print("value : ",round(newnum,2))
print("***end***")


# 
