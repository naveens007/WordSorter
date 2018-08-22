#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""

#   Word Sorter
#   Copyright (C) 2018  Hemanya Sharma

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

#   Version: 1.0.1 - Build 1.2

#   special chars are the first priority and are sorted first.
#   numbers are the second priority and are sorted second.
#   alphabets are the third priority and are sorted third (UPPERCASE are sorted before lowercase).

#   names are to be entered as 'Hemanya-Sharma' or 'Rob-Mctodd' not 'roB-McTodd' or 'hemanyA sHarMA'

"""


author = "Hemanya Sharma"
version = "1.0.1 - Build 1.2"
yelp = "Program to alphabetically sort the words from a string provided by the user."

class colors:
    GREEN = '\033[32m'
    RED = '\033[31m'
    ENDC = '\033[m'

def sort (yer_word):
    num = 1
    words = yer_word.split() # Breakdown the string into a list of words
    words.sort() # Sort the words
    print("The sorted words are:\n") # Display the sorted words
    for sort in words:
       print (str(num) + "." , colors.GREEN + sort , colors.ENDC)
       num = num + 1
    return


def mains ():
    yer_word = input("Enter the words to sort: ")
    if  len(yer_word.split()) > 0:
        sort (yer_word)
        return "Called"
    else:
        print (colors.RED + "ERROR: Enter some words to sort! 😒" , colors.ENDC)
        return "Error"


if (__name__ == '__main__'):
    mains ()


################
