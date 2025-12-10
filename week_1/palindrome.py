class Solution:
    def isPalindrome(self, x: int) -> bool:
        # sayıyı string'e çevir
        s = str(x)
        # tersini al ve karşılaştır
        return s == s[::-1]