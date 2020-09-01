#!/usr/bin/env python
# coding: utf-8
#Case Study III
#Domain –Telecomfocus –OptimizationBusiness challenge requirementLifeTel Telecomis the latest entrant in the highly competitive Telecom market of Singapore.  It issues SIM to the verified users.  Till now verification was manual through the photocopy of approved id card document. However,government has recently introduced Social ID called Reference ID which is mapped to fingerprint of user.LifeTel should now verify user against the fingerprint and Reference IDKey issuesBuild a system where when user enters Reference ID it is encrypted, so that hackers cannot view the mapping of Reference ID and finger printConsiderationsSystem should be secureData volume-NAAdditional information-NABusiness benefitsCompany will be able to quickly issue SIM to user and expected gain in volume is approximately 10 times as the manual process of verification is replaced with secure automated systemApproach to SolveYou have to use fundamentals of Python taught in module 11.Read the input from command line –Reference ID2.Check for validity –it should be 12 digits and allows on number and alphabet

# In[8]:

import re
decrypted = b"ABCDEFGHIJKLMNOPQRSTUVWXYZ@$_0123456789 "
encrypted = b"CVBNMYUIOPLKJHGFDSAZXQWERT_$@9876543210 "
ch=input("enter the name:")

encrypt_table = bytes.maketrans(decrypted, encrypted)
decrypt_table = bytes.maketrans(encrypted, decrypted)

result = ''
message = ''


flag=0
ch1=ch.upper()
if (len(ch1)==12):
    enc_dec=input("for encrypt enter  1 and for decrypt enter 2:")
else:
    flag = -1

while True:   
    if (len(ch1)!=12): 
        break
    elif not re.search("[A-Z]", ch1): 
        flag = -1
        print("doesnot contain the characters")
        if(enc_dec=="2"):
            flag = 0
        break
    elif not re.search("[0-9]", ch1): 
        flag = -1
        print("doesnot contain the digits")
        if(enc_dec=="2"):
            flag = 0
        break
    elif not re.search("[_@$]", ch1): 
        flag = -1
        print("doesnot contain the special_charcters")
        if(enc_dec=="2"):
            flag = 0
        break
    else: 
        flag = 0
        print("Valid Password")
        break 
if flag ==-1: 
    print("Not a Valid Password ") 

if(flag==0):

        if enc_dec == '1':
            result = ch1.translate(encrypt_table)
            print(result + '\n\n')

        elif enc_dec == '2':
            result = ch1.translate(decrypt_table)
            print(result + '\n\n')

        elif (enc_dec != '1') and (enc_dec != '2'):
            print('You have entered an invalid input, please try again. \n\n')