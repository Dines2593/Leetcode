class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        elif x<10:
            return True
        x = list(str(x))
        if x==list(reversed(x)):
            return True
        else:
            return False

