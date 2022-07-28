"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


Example 1:

Input: x = 123
Output: 321


Example 2:

Input: x = -123
Output: -321


Example 3:

Input: x = 120
Output: 21
"""


def reverse(x: int) -> int:
	x_str = str(x)
	upperbound_int32_limit = 2_147_483_647
	lowerbound_int32_limit = -2_147_483_648

	reversed_int_str = x_str[::-1]

	if list(reversed_int_str)[len(reversed_int_str) - 1] == '-':
		reversed_int_str = f'-{reversed_int_str[:-1]}'
	
	reversed_integer = int(reversed_int_str)
	
	if reversed_integer > upperbound_int32_limit or reversed_integer < lowerbound_int32_limit:
		return 0
	return reversed_integer
