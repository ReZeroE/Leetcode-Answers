class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if len(str(x)) == 1: return x
        
        x = str(x)
        sign = ''
        if x[0] == '-': 
            sign = '-'
            x = x.strip('-')

        result = sign + x[::-1].lstrip('0')
        if -2147483648 <= result <= 2147483647: return 0
        
        return result