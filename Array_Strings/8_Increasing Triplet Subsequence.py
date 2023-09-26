class Solution:
    def increasingTriplet(self, nums) -> bool:
        seq = [float('inf')]*3
        for num in nums:
            for i in range(len(seq)):
                if i == 2:
                    return True
                elif  num <= seq[i]:
                    seq[i] = num
                    break
        return False