# # Define original string
# original_str = "Hello"
# # Reverse the original string using reversed() function
# #and join the characters back together into a new string
# reversed_string = ''.join(reversed(original_str))
# # Print the reversed string
# print(reversed_string)

# Function checks for palindrome
def is_palindrome(word):
    # Reverse the string with the use of reverse() and join() method
    result = ''.join(reversed(word))
    return word == result

# Test. Verification of palindrome function
def test_palindrome():
     input_str = "racecar"
     reversed_result = is_palindrome(input_str)
     assert reversed_result == True
     print("Test is successful as "+input_str+ " is palindrome.")

 # Write the function to find the factorial of a no
# Import math module to access the mathematical function

import math

# Define a function to find out the factorial of a no

def factorial(number):
    return math.factorial(number)
# Test. Verification of factorial function
def test_factorial():
    input_number = 5
    result = factorial(input_number)
    assert result == 120
    print(f"Test is passed as the factorial of {input_number} is equal to {result}")







