#!/usr/bin/env python3
# -*- coding: iso-8859-15 -*-
# Copyright 2017 Knock Mail.
# Written by: * Alisson Moretto - 4w4k3
# https://github.com/4w4k3/KnockMail
# Licensed under the BSD-3-Clause
import os
import sys
import argparse
from validate_email import validate_email


results = []


### Argparser

## argparse arguments
parser = argparse.ArgumentParser(description="email verification utility")

## Scan parser
parser.add_argument('--email', help='email(s) to scan', metavar='EMAIL')
parser.add_argument('-f', '--file', help='file with email(s) to check')

args = parser.parse_args()


BLUE, RED, WHITE, YELLOW, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;32m', '\033[0m'

def search():
    if args.file:
        inputfile = args.file
    else:
        inputfile = input('Path to file with email addresses to scan: ')
		
    with open(inputfile) as infile:
        for line in infile:
            results.append(line.strip())
    count = 0
    for i in results:
        is_valid = validate_email(i,verify=True)
        count += 1
        if is_valid == True:
            sys.stdout.write(GREEN + "[*] FOUND - [" + i + "] "+ BLUE + "{line " + str(count) + "}\n" + END)
        else:
            sys.stdout.write(RED + "[!] NOTFOUND - [" + i + "]" + BLUE + " {line " + str(count) + "}\n" + END)

def single():
    if args.email:
        ema = str(args.email)
    else:
        ema = input('Email address to verify: ')
    is_valid = validate_email(ema,verify=True)
    if is_valid == True:
        sys.stdout.write(GREEN + "[*] FOUND - [" + ema + "]\n" + END)
    else:
        sys.stdout.write(RED + "[!] NOTFOUND - [" + ema + "]\n" + END)

def banner():
    os.system('clear')
    sys.stdout.write(WHITE + '''
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
				 	v1.0.1   
     [-                                              -]
     ''')

def menu():
    print('''
    -Usage- Select an option:

     {0}[{1}1{0}]{1}     Perform a search of emails from specified file.
     {0}[{1}2{0}]{1}     Single search for specified email.
     {0}[{1}E{0}]{1}     Exit.
    '''.format(RED, END))
    while True:
        try:
            ask = input("KKM > ").format(RED, END)
            if ask.upper() == "1":
                search()
            if ask.upper() == "2":
                single()
            if ask.upper() == "E":
                sys.exit(0) 
        except:
            print("\nThank you for using Knock Mail.")
            sys.exit(0)

def main():
    if args.email:
        single()
    elif args.file:
        search()
    else:
        banner()
        menu()

if __name__ == '__main__':
    main()
