class Solution:
    def reverse(self, x: int) -> int:
        new_int = 0
        negative = False
        if x < 0:
            x = -x
            negative = True
        while(x != 0):
            new_int = new_int*10 + x%10
            x = x//10
        if negative == True:
            new_int = -new_int
        if pow(-2,31) < new_int and new_int < pow(2,31) -1:
           return new_int
        return 0