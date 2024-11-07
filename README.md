# Advanced_pattern_match
This program takes 2 user string inputs:
1) A pattern string: can be any string, that also contains either "?" or "*" characters, that you want to match
2) A word string: a second string that can also be anything, to try and match with your pattern string

After taking those 2 inputs, the strings are matched together through a recursive function with 3 base cases:
1) If both the word and pattern are empty, the result is immediately returned as True
2) If either the pattern or word are empty, but not both of them, then the result is returned as False
3) If the pattern is at least 1 character long, the current pattern character is "*", and the word is empty, then the result is returned as False

If either the pattern is at least 1 character long and the current pattern character is "?", or the current pattern and word characters match, the function makes a recursive call with the remaining characters.

If the pattern and word are at least 1 character long, and the current pattern character is "*", there are 3 possible recursive function calls:
1) A call that considers the current character in the word and ignores the current pattern character
2) A call that ignores the current character in the word but not the current pattern character
3) A call that ignores the current character in the pattern and the current word character

The main function will keep asking for the pattern and word inputs until the pattern string is "q".
