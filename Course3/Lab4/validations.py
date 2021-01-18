#!/usr/bin/env python3
"""
Importing necessary modules
"""
import re

"""Function that checks if the received username matches the required conditions."""
def validate_user(username, minlen):
    
    #Checks if the first character is a alphabet
    if not username[0].isalpha(): 
        return False

   #Checks if minlen is less than 1
    if minlen < 1: 
        raise ValueError("minlen must be at least 1")

    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False

    # Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[a-z0-9._]*$', username):
        return False
        
    # Usernames can't begin with a number
    if username[0].isnumeric():
        return False
    return True


print(validate_user("blue.kale", 3))  # True
print(validate_user(".blue.kale", 3))  # Currently True, should be False
print(validate_user("red_quinoa", 4))  # True
print(validate_user("_red_quinoa", 4))  # Currently True, should be False

