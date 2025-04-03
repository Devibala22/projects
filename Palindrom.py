"""         Checks if a string is a palindrome (reads the same backward as forward). """
def check_palindrome(s):

   return s == s[::-1]

# Test case
string1 = "madam"
print(check_palindrome(string1)) 

string2 = "hello"
print(check_palindrome(string2))
