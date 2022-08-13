"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif


Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


Example 2:

Input: numRows = 1
Output: [[1]]
"""


from typing import List


def generate(numRows: int) -> List[List[int]]:
	result = []

	# makes the triangle grid based on given number of rows
	size_count = 0
	for i in range(numRows):
		size_count += 1
		result.append([0] * size_count)
	
	# fills in the grid edges with 1's
	for i in range(len(result)):
		for j in result[i]:
			result[i][0] = 1
			result[i][len(result[i]) - 1] = 1

	# fills in the rest of the grid
	for i in range(len(result)):
		for j in range(len(result[i]) - 2):
			if 0 not in result[i]:
				continue
			result[i][j + 1] = result[i - 1][j] + result[i - 1][j + 1]
	return result
	