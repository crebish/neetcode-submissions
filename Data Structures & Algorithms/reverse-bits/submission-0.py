class Solution:
    def reverseBits(self, n: int) -> int:
        
        ans = 0

        for _ in range(32):
            temp = n & 1

            ans = ans << 1
            ans = ans | temp
        
            n = n >> 1

        return ans