"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"


Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
	if len(strs) == 1:
		return strs[0]

	result: str = ''

	smallest_item = min(strs, key=len)
	for i in range(len(smallest_item)):
		letter = list(smallest_item)[i]

		count = 0
		for j in range(len(strs)):
			if letter == list(strs[j])[i]:
				count += 1
		if count == len(strs):
			result += letter
		else:
			break

	return result
