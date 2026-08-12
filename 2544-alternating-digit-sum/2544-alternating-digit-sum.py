class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = str(n)
        total = 0

        for i,digit in enumerate(digits):
            if i%2==0:
                total +=int(digit)
            else:
                total -=int(digit)
        return total
        