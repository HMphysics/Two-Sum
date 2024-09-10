class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        
        # Traverse the list of numbers
        for i, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            
            # Check if the complement is already in the dictionary
            if complement in num_map:
                # If it is, return the indices of the complement and the current number
                return [num_map[complement], i]
            
            # If not, add the current number to the dictionary with its index
            num_map[num] = i




        
