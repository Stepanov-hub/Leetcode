# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:

        start = 1
        end = n

        while start < end - 1:
            el_to_check = int((start + end) / 2)

            if isBadVersion(el_to_check):
                end = el_to_check
            else:
                start = el_to_check

        return start if isBadVersion(start) else end
