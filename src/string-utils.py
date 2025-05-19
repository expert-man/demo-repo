# src/string_utils.py
def reverse_string(s):
    return s[::-1]

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

def is_palindrome(s):
    s_clean = ''.join(c.lower() for c in s if c.isalnum())
    return s_clean == s_clean[::-1]
