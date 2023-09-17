class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        greatest = max(candies)
        return [i+extraCandies>=greatest for i in candies]