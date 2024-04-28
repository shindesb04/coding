class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        n = len(digits) - 1
        carry = 1
        num = digits[n]
        if num < 9:
            digits[n] += 1
            return digits
            
        while n >= 0 and carry:
            temp = digits[n] + carry
            carry = temp // 10
            num = temp % 10
            digits[n] = num
            n -= 1
        
        if carry:
            digits.insert(0,carry)    
        return digits
         