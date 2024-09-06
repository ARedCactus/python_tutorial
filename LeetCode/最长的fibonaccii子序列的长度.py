class Solution:
    def lenLongestFibSubseq(arr) -> int:
        n = len(arr)
        if n == 0:
            return 0
        dict_ = {}
        for i in range(n):
            dict_[arr[i]] = i
        list_ = [[0 for i in range(n)] for j in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                list_[i][j] = 2
        Max_len = 0
        for i in range(n):
            for j in range(i+1, n):
                diff = arr[j] - arr[i]
                if diff in dict_:
                    index = dict_[diff]
                    if index < i:
                        list_[i][j] = max(list_[i][j], list_[index][i]+1)
                Max_len = max(Max_len, list_[i][j])
        return Max_len if Max_len>2 else 0
    
if __name__ == '__main__':
    list_ = [1,2,3,4,5,6,7,8]
    num = Solution.lenLongestFibSubseq(list_)
    print(num)
