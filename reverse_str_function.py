# Function that reverse a string
def reverse_string(word):
    return ''.join(reversed(word))
# Test. Verification of reverse_string function
def test_reverse_string():
    input_str = "TripleTen"
#perform the reverse operation
    reversed_str = reverse_string(input_str)
#Check if the reversed string matches the expected output
    assert reversed_str == "neTelpirT"
    print("Test passed " + input_str + "'s reversed is " + reversed_str)
