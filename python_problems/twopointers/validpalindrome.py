"""
Approach/Notes: two pointers
Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        length: int = len(s)
        p1 = 0
        p2 = length - 1
        while p1 < p2:
            if not s[p1].isalnum():
                p1 += 1
                continue
            if not s[p2].isalnum():
                p2 -= 1
                continue
            if s[p1].lower() != s[p2].lower():
                return False
            p1 += 1
            p2 -= 1
        return True
