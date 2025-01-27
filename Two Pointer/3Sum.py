class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Step 1: Sort the array to enable the two-pointer approach
        nums.sort()
        n = len(nums)
        answer_list = []

        # Step 2: Iterate through the array with the first pointer
        for i in range(n):
            # If the current number is greater than 0, no triplet can sum to 0
            if nums[i] > 0:
                break

            # Skip duplicate values for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Step 3: Use two pointers to find pairs that sum with nums[i] to 0
            low, high = i + 1, n - 1
            while low < high:
                total = nums[i] + nums[low] + nums[high]

                if total == 0:
                    # Found a triplet
                    answer_list.append([nums[i], nums[low], nums[high]])

                    # Skip duplicate values for the second number
                    while low < high and nums[low] == nums[low + 1]:
                        low += 1

                    # Skip duplicate values for the third number
                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1

                    # Move both pointers after recording a valid triplet
                    low += 1
                    high -= 1

                # Adjust pointers based on the sum
                elif total < 0:
                    low += 1  # Increase the sum
                else:
                    high -= 1  # Decrease the sum

        return answer_list

        """
        Summary Logic:
        1. Sort the array to leverage the two-pointer approach.
        2. Iterate through the array with a fixed pointer `i` (first element of the triplet).
           - If the value at `i` is greater than 0, stop processing (no triplet can sum to 0).
           - Skip duplicate values for `nums[i]` to avoid repeated triplets.
        3. Use two pointers (`low` and `high`) to find a pair that sums with `nums[i]` to 0:
           - If the sum equals 0, store the triplet in the result and move both pointers.
           - Skip duplicate values for `nums[low]` and `nums[high]` to ensure unique triplets.
           - If the sum is less than 0, increment `low` to increase the total.
           - If the sum is greater than 0, decrement `high` to decrease the total.
        4. Continue until the two pointers meet.
        5. Return the list of unique triplets.
        """
