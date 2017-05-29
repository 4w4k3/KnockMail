#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
# Copyright 2017 Knock Mail.
# Written by: * Alisson Moretto - 4w4k3
# https://github.com/4w4k3/KnockMail
# Licensed under the BSD-3-Clause
from os import system
from sys import stdout, exit
from validate_email import validate_email
results = []
system('clear')
BLUE, RED, WHITE, YELLOW, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;32m', '\033[0m'
def search():
    inputfil = raw_input("Type the path of file containing a list of emails: ")
    with open(inputfil) as inputfile:
        for line in inputfile:
            results.append(line.strip())
    count = 0
    for i in results:
        is_valid = validate_email(i,verify=True)
        count += 1
        if str(is_valid).upper() == "TRUE":
	    stdout.write(GREEN + "[*] FOUND - [" + i + "] "+ BLUE + "{line " + str(count) + "}\n" + END)
        else:
            stdout.write(RED + "[!] NOTFD - [" + i + "]" + BLUE + " {line " + str(count) + "}\n" + END)

def single():
    ema = raw_input("Type the email to search: ")
    is_valid = validate_email(ema,verify=True)
    if str(is_valid).upper() == "TRUE":
        stdout.write(GREEN + "[*] FOUND - [" + ema + "]\n" + END)
    else:
	stdout.write(RED + "[!] NOTFD - [" + ema + "]\n" + END)

stdout.write(WHITE + '''
By: @4w4k3
https://github.com/4w4k3
[-                                              -]''' + RED + '''

                                                   
 _|    _|                                _|        
 _|  _|    _|_|_|      _|_|      _|_|_|  _|  _|    
 _|_|      _|    _|  _|    _|  _|        _|_|      
 _|  _|    _|    _|  _|    _|  _|        _|  _|    
 _|    _|  _|    _|    _|_|      _|_|_|  _|    _|  
                                               mail''' + END + '''
            [ ]''' + RED + ' Knock Knock Mail ' + END + '''[ ]
				 	v1.0   
[-                                              -]
''')
print '''
-Usage- Select an option:

  {0}[{1}1{0}]{1}     Perform a search of emails from specified file.
  {0}[{1}2{0}]{1}     Single search for specified email.
  {0}[{1}U{0}]{1}     Update.
  {0}[{1}E{0}]{1}     Exit.
'''.format(RED, END)
while True:
    try:
        ask = raw_input("KKM > ").format(RED, END)
    	if ask.upper() == "1":
            search()
	if ask.upper() == "2":
            single()
        if ask.upper() == "E":
            exit(0) 
    except:
        print "\nThank you for use Knock Mail."
        exit(0)
