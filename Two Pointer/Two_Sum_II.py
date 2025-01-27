class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            else:
                right -= 1

"""
We are using the two-pointer approach here. First, we assign the left pointer to index 0 and the right pointer to index n-1.
While `left` is less than `right` (pointers don’t cross):
- Calculate the total of the values at the left and right pointers.

**Case 1 (Best Case):**
If the sum of index 0 (`left`) and index n-1 (`right`) equals the target, simply return `left + 1` and `right + 1`.

**Case 2:**
When the total is less than the target, increase the left pointer by 1 because the array is sorted in ascending order.

**Case 3:**
When the total is greater than the target, decrease the right pointer by 1.
"""
