from dataclasses import dataclass


@dataclass
class DevisionResult:
    is_save: bool
    result: int


class Solution:
    def _check(self, n: int, checked_factor: int) -> DevisionResult:
        if n % checked_factor == 0:
            return DevisionResult(
                is_save=True,
                result=n / checked_factor,
            )
        else:
            return DevisionResult(
                is_save=False,
                result=n,
            )

    def check(self, n: int, checked_factor: int) -> int:
        devision_result = self._check(
            n=n,
            checked_factor=checked_factor,
        )

        while devision_result.is_save and devision_result.result > 1:
            devision_result = self._check(
                n=devision_result.result,
                checked_factor=checked_factor,
            )

        return devision_result.result

    def save_division(self, n: int, checked_factors: frozenset) -> int:
        for checked_factor in checked_factors:
            n = self.check(
                n=n,
                checked_factor=checked_factor,
            )

            if n == 1:
                break

        return n

    def isUgly(self, n: int) -> bool:

        if n == 1:
            return True
        elif n <= 0:
            return False

        n = self.save_division(n=n, checked_factors=frozenset((5, 3, 2)))

        return True if n == 1 else False


# class Solution:
#     def isUgly(self, n: int) -> bool:
#         if n <= 0:
#             return False

#         while n % 2 == 0:
#             n/=2
#         while n % 3==0:
#             n/=3
#         while n % 5 == 0:
#             n/=5

#         return n==1
