class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        srt_nums = sorted(nums)
        left = 0 
        right = len(srt_nums) - 1
        while left < right:
            curr_sum = srt_nums[left] + srt_nums[right]
            if curr_sum == target:
                if srt_nums[left] != srt_nums[right]:
                    return [nums.index(srt_nums[left]),nums.index(srt_nums[right])]
                else:
                    cache = srt_nums[left]
                    first = nums.index(srt_nums[left])
                    nums.pop(first)
                    second = nums.index(cache)+1
                    return [first, second]
            elif curr_sum < target:
                left+=1
            else:
                right-=1
        return -1
