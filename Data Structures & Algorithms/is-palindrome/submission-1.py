class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = ""
        for ch in s:
            if ch.isalnum():
                n += ch.lower()
        return n == n[::-1]

