"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:

Input: s = "anagram", t = "nagaram"
Output: true


Example 2:

Input: s = "rat", t = "car"
Output: false
"""


def isAnagram(s: str, t: str) -> bool:
	if len(s) != len(t):
		return False

	s_letters = list(s)
	t_letters = list(t)

	for i in s_letters:
		if i in t_letters:
			t_letters.remove(i)

	if len(t_letters) == 0:
		return True
	return False
