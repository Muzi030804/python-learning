class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for num in nums:
            hash[num] = hash.get(num,0)+1
        print(hash)

        for key, value in hash.items():
            if value > 1:
                return True
        return False


print(Solution().containsDuplicate([1,2,3,4,4]))