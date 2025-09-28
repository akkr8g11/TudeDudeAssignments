def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    return reverse_string(s) == s

def count_words(s):
    return len(s.split()) 