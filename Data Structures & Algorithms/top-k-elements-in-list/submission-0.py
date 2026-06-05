class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_maps = {}
        n = len(nums)
        for i in range(n):
            hash_maps[nums[i]] = hash_maps.get(nums[i],0)+1
            
        sorted_items = sorted(
            hash_maps.items(),
            key=lambda x: x[1],
            reverse=True
        )

        result = []

        for i in range(k):
            result.append(sorted_items[i][0])

        return result
