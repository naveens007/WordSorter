#!/usr/bin/python3

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

#   Version: 1.0.0 - Build 3.4

#   special chars are the first priority and are sorted first.
#   numbers are the second priority and are sorted second.
#   alphabets are the third priority and are sorted third. (UPPERCASE are sorted before lowercase)

#   names are to be entered as 'Hemanya-Sharma' or 'Bill-Gates' not 'bILL-gAtEs' or 'hemanyA sHarMA'

"""


author = "Hemanya Sharma"
version = "1.0.0 - Build 3.4"
yelp = "Program to sort alphabetically the words from a string provided by the user"

class colors:
    ENDC = '\033[m'
    GREEN = '\033[32m'

def sort (yer_word):
    num = 1
    # breakdown the string into a list of words
    words = yer_word.split()
    # sort the list
    words.sort()
    # display the sorted words
    print("The sorted words are:\n")
    for sort in words:
       print( str(num) + "." , colors.GREEN + sort , colors.ENDC )
       num = num + 1

def mains ():
    yer_word = input("Enter the words to sort: ")
    sort (yer_word)


if (__name__ == '__main__'):
    mains ()

################
