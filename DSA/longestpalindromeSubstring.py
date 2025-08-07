#findout the longest palindromic substring in a given string

def is_palindrome(s):
    return s == s[::-1]

def longest_palindrome_substring(s):
    n = len(s)
    for i in range (n, 0, -1):
        for j in range(n - i + 1):
            substring = s[j:j + i]
            if is_palindrome(substring):
                return substring
    return ""   

str = "startraffic"
print("Longest palindromic substring:", longest_palindrome_substring(str))