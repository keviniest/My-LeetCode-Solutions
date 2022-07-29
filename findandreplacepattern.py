"""
Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.


Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.


Example 2:

Input: words = ["a","b","c"], pattern = "a"
Output: ["a","b","c"]
"""

from typing import List


def findAndReplacePattern(words: List[str], pattern: str) -> List[str]:
	def get_code(s: str) -> List[int]:
		s_list = list(s)
		s_codes = {}
		count = 0
		for i in range(len(pattern)):
			if i == 0:
				s_codes[s_list[0]] = 0
				count += 1
			else:
				s_codes[s_list[i]] = count
				count += 1
		code: List[int] = []
		for i in s_codes.keys():
			code.append(s_codes[i])
		return code

	result = []
	pattern_code = get_code(pattern)
	for i in words:
		if pattern_code == get_code(i):
			result.append(i)
	return result
