class Solution:
    def romanToInt(self, s: str) -> int:

        dict_consts = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90,
                       'CD':400, 'CM':900}

        it = 0
        len_s = len(s)
        num = 0

        while it+1 < len_s:
            if s[it:it+2] in dict_consts:
                num += dict_consts[s[it:it+2]]
                it += 2
            else:
                num += dict_consts[s[it]]
                it += 1

        if it < len_s:
            num += dict_consts[s[it]]

        return num
        
        
        
#class Solution:
#    def romanToInt(self, s: str) -> int:
#        roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
#        number=0
#        for i in range(len(s)-1):
#            if roman[s[i]] < roman[s[(i+1)]]:
#                number-=roman[s[i]]
#            else:
#                number+=roman[s[i]]
#        return number+roman[s[-1]]
