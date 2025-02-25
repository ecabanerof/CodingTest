# In order to ensure maximum security, the developers at Amazon employ multiple encryption methods to keep user data protected. 
# In one method, numbers are encrypted using a scheme called 'Pascal Triangle'. When an array of digits is fed to this system, 
# it sums the adjacent digits. It then takes the rightmost digit (least significant digit) of each addition for the next step. 
# Thus, the number of digits in each step is reduced by 1. This procedure is repeated until there are only 2 digits left, and 
# this sequence of 2 digits forms the encrypted number. Given the initial sequence of the digits of numbers, find the encrypted number. 
# You should report a string of digits representing the encrypted number. Example numbers = [4, 5, 6, 7] Encryption occurs as follows: 
# https://hrcdn.net/s3_pub/istreet-assets/5SpVmNFwk1wwfdWnKuiBHA/srgfwae%20(1).png Hence, the encrypted number formed is 04.

# Complete the function findNumber in the editor below The first line contains an integer, n , the number of elements in Each line i of the n subsequent lines (where 0 ≤ i < n) contains an integer that describes numbers[i]

# The numbers 3,6,9 and 12 are multiples of 3 (but not 5), so print Fizz on those lines The numbers 5 and 10 are multiples of 5 (but not 3), 
# so print Buzz on those lines The number 15 is a multiple of both 3 and 5, ), so print FizzBuzz on that line. None of the other values is 
# a multiple of either 3 or 5 , so print the value of i on those lines.

# for more info STDIN         FUNCTION -----         -------- 4        →    numbers[] size, n = 4 1        →    numbers = [1, 2, 3, 4] 2 3 4 sample output 82
# The encryption occurs as follows: [1, 2, 3, 4] → [3, 5, 7] → [8, 2]

#!/bin/python3

import math 
import os 
import random 
import re 
import sys

# Complete the 'findNumber' function below.
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY numbers as parameter

# Explanation
# We start with a list of digits.
# We add each pair of neighboring digits.
# We take only the last digit (mod 10) of each sum and make a new list.
# We repeat the process until only two digits remain.
# Those two digits form the final encrypted number.

def findNumber(numbers):
    # Continue reducing the list until only 2 digits remain
    while len(numbers) > 2:
        temp = []
        # Sum each pair of digits and store the last digit of the sum
        for i in range(len(numbers) - 1):
            s = numbers[i] + numbers[i + 1]
            temp.append(s % 10)
        # Update numbers with the newly formed list
        numbers = temp
    # Combine the remaining two digits into a string and return
    return f"{numbers[0]}{numbers[1]}"



if name == 'main': 
  n = int(input().strip())
