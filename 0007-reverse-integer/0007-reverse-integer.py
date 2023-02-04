class Solution:
    def reverse(self, x: int) -> int:
        new_int = ''
        x = str(x)
        for index in range(len(x)-1,-1,-1):
            new_int += x[index]
        if new_int[-1] == '-':  
            if int('-'+new_int[:-1]) > pow(-2,31):
                return int('-'+new_int[:-1])
            return 0
        elif int(new_int) < pow(2,31) - 1:
            return int(new_int)
        return 0