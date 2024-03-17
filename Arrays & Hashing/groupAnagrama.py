# Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:

# Input: strs = [""]
# Output: [[""]]

# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]


# TestCase: 
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# aet = [eat, tea, ate]
# atn = [tan, nat]
# abt = [bat]


def groupAnagrams(strs):
        d = {}
        for i in strs:
            currSorted = "".join(sorted(i))
            if currSorted not in d:
                d[currSorted] = [i]
            else:
                d[currSorted].append(i)
                
        res = []
        for k,v in d.items():
            res.append(v)
        return res
