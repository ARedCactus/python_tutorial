from collections import Counter

class Solution:
    def minCostToMoveChips(self, position: list[int]) -> int:
        list_ = Counter(x % 2 for x in position)
        return min(list_[0], list_[1])
    
if __name__ == '__main__':
    list_ = [1 ,2, 4, 5, 5]
    num = Solution().minCostToMoveChips(list_)
    print(num)
    
