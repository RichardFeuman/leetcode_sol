class Solution:
    def is_pal(self, seq):
        left = 0
        right = len(seq) - 1
        while left < right:
            if seq[left] != seq[right]:
                return False
            left+=1
            right-=1
        return True
    
    
    def longestPalindrome(self, s: str) -> str:
        start = 0
        max_len = 0
        head = s[:1]
        if all([ch == head for ch in s]):
            return s
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.is_pal(s[i:j+1])  and len(s[i:j+1]) > max_len:
                    start = i
                    max_len = len(s[i:j+1])
        return s[start:start+max_len] 
