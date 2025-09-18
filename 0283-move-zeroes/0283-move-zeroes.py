class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Pointer for the position to place the next non-zero element
        insert_pos = 0

        # Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1

        # Fill the remaining positions with zeros
        for i in range(insert_pos, len(nums)):
            nums[i] = 0