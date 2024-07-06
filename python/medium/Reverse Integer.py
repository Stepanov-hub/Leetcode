class Solution:
    def reverse(self, x: int) -> int:

        sign = 1
        return_value = 0
        int_max = 2147483647
        int_min = -2147483648

        if x < 0:
            sign = -1
            x = abs(x)

        while x != 0:
            # if return_value > int_max/10 or return_value
            return_value = return_value * 10 + x % 10
            x = int(x / 10)

        return_value = return_value * sign

        return return_value


a = Solution()
input = -123
print(a.reverse(input))
