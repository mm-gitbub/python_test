# Function to check for palindrome
def is_palindrome(word):
    # Reverse the string using reversed() and join().
    reverse_result =  ''.join(reversed(word))
    return word == reverse_result

# Test. Verification of is_palindrome function

def test_palindrome():
    # Define the input string
    input_str = "racecar"

    # Perform the palindrome check
    result = is_palindrome(input_str)
    # Check if the result is True for a palindrome
    assert result == True
    print("Test is successful "+ input_str +" is perfectly palindrome")