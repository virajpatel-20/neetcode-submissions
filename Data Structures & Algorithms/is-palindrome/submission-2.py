class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []

        for ch in s:
            if ch.isalnum():
                chars.append(ch.lower())

        s1 = "".join(chars)
        if s1 == s1[::-1]:
            return True
        else:
            return False

