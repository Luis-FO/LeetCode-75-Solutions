class Solution:
    def maxArea(self, height):
        h1, h2, area = 0, len(height) - 1, 0
        while h1<h2:
            area = max(area, (h2-h1)*min(height[h1], height[h2]))
            if height[h1] > height[h2]:
                h2-=1
            else:
                h1+=1

        return area