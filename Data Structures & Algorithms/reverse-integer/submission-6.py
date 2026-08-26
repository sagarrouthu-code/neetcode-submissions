class Solution:
    def reverse(self, x: int) -> int:
        original_x = x
        

        if original_x < 0:
            sign = -1
            original_x = abs(original_x)
        else:
            sign = 1
        rev = 0
        
        while original_x > 0:
            digit = original_x % 10
            rev = rev * 10 + digit
            original_x = original_x // 10
        
        rev = rev * sign
      

        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        else:
            return rev