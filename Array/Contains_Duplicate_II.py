class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Dictionary to store the last seen index of each number
        value_indices = {}
        for index, num in enumerate(nums):
            # Check if the number exists in the dictionary and is within the range
            if num in value_indices and index - value_indices[num] <= k:
                return True
            # Update the last seen index for the number
            value_indices[num] = index
        return False
