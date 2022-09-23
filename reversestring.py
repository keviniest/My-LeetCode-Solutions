"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.


Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]


Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""


from typing import List


# iter 1
def reverseString(s: List[str]) -> None:
	"""
	Do not return anything, modify s in-place instead.
	"""
	for i in range(len(s) // 2):
		temp = s[i]
		s[i] = s[len(s) - 1 - i]
		s[len(s) - 1 - i] = temp
