class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_maps = {}
        n = len(nums)
        for i in range(n):
            hash_maps[nums[i]] = hash_maps.get(nums[i], 0) + 1
            if hash_maps[nums[i]] > 1:
                return True
          
        return False



        
        