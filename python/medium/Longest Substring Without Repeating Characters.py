class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        len_s = len(s)

        if len_s == 0:
            return 0

        return_value = 0
        dict_s = {}
        intermediate_value = 0
        start = 0

        for i in range(len_s):
            pos = dict_s.get(s[i], -1)
            if pos < start:
                intermediate_value += 1
                dict_s[s[i]] = i
            else:
                if return_value < intermediate_value:
                    return_value = intermediate_value
                intermediate_value = i - pos
                dict_s[s[i]] = i
                start = pos + 1

        if return_value<intermediate_value:
            return intermediate_value
        else:
            return return_value