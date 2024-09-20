class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def is_palindrome(s):
            return s == s[::-1]
        pal= is_palindrome(s)
        if pal:
            
