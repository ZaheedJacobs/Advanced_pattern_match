# Module to recursively determine whether a given pattern matches a given word

def match(pattern: str, word: str)-> bool|None:
    # Match user-specified pattern and word

    # We reach the end if both strings are empty
    if len(pattern) == 0 and len(word) == 0:
        return True
    
    # If either string is empty, immediately return False
    elif pattern == "" or word == "":
        return False
    
    # Recursively call if pattern contains "?" or the current characters
    # of both strings match
    elif (len(pattern) >= 1 and pattern[0] == "?") or (len(pattern) != 0 and len(word) != 0 and pattern[0] == word[0]):
        return match(pattern[1:], word[1:])
    
    # Return False if pattern contains "*" but word is empty
    elif len(pattern) >= 1 and pattern[0] == "*" and len(word) == 0:
        return False
    
    # Three possible recursive calls if pattern contains "*"
    # 1) Consider the current character in word
    # 2) Ignore the current character in word
    # 3) Ignore the current character in pattern
    elif len(pattern) >= 1 and pattern[0] == "*" and len(word) >= 1:
        return match(pattern[1:], word) or match(pattern[1:], word[1:]) or match(pattern, word[1:])
    
    return False

def main()-> None:
    user_pattern: str = input("Enter a pattern that you want to match:\n")
    
    while user_pattern.lower() != "q":
        user_word: str = input("Enter a word that you want the pattern to match with:\n")
        if match(user_pattern, user_word):
            print("The word and pattern match!")

        else:
            print("Unfortunately, the word and pattern do not match.")
        print()
        user_pattern: str = input("Enter a pattern that you want to match:\n")

if __name__ == "__main__":
    main()