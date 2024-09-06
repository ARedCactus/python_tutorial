import string

class Solution:
    def minAddToMakeValid(self, str_: str) -> int:
        ans = left = 0
        for x in str_:
            if x == "(":
                left += 1
            elif left > 0:
                left -= 1
            else:
                ans += 1
        return ans + left


if __name__ == '__main__':
    str_ = "))((())))"
    num = Solution().minAddToMakeValid(str_)
    print(num)