class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_o_n_num=(n*(n+1))//2
        sum_num=sum(nums)
        misnum=sum_o_n_num-sum_num
        return misnum