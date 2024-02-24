from collections import deque

def is_palindrome(s):
    # Convert the string to lowercase and remove spaces
    s = s.lower().replace(" ", "")
    
    # Create a deque and add characters of the string to it
    char_deque = deque(s)
    
    # Iterate until the deque has only one or no elements left
    while len(char_deque) > 1:
        # Pop characters from both ends of the deque
        first = char_deque.popleft()
        last = char_deque.pop()
        
        # If the characters at both ends are not equal, it's not a palindrome
        if first != last:
            return False
    
    # If the loop completes without returning False, the string is a palindrome
    return True

# Test cases
print(is_palindrome("racecar"))   # True
print(is_palindrome("hello"))      # False
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("Was it a car or a cat I saw"))  # True
