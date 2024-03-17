# Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

# Algorithm:
# sort both the strings and compare.


def isAnagram(s: str, t: str) -> bool:
    s = "".join(sorted(s))
    t = "".join(sorted(t))
    return s==t