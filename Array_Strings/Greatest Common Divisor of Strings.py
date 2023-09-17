class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''

        def gcd(len_a, len_b):
            if len_b == 0:
                return len_a

            return gcd(len_b, len_a % len_b)

        length = gcd(len(str1), len(str2))
        return str1[:length]