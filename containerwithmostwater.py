"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.


Example 2:

Input: height = [1,1]
Output: 1
"""


from typing import List

# wip
# this cant even pass the lc testcases bc its slow af
def maxArea(height: List[int]) -> int:
	largest = 0
	for i in range(len(height)):
		for j in range(len(height)):
			container_base = max(i, j) - min(i, j)
			container_height = min(height[i], height[j])
			container_size = container_base * container_height

			if container_size > largest:
				largest = container_size
	return largest
