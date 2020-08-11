# Note that brute-force solution of this question is:
# O(m.n) time complexity and O(1) space complexity.
# THerefore it is suggested to solve this problem with hash map.
# There is a python library called "counter"
# We actually preprocess the magazine parameter.
# It's a single-pass algorithm O(n) for time and O(n) for space complexities.

import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine:str) -> bool:
        mag_dict = collections.defaultdict(int)
        for char in magazine:
            mag_dict[char] += 1
        for char in ransomNote:
            mag_dict = mag_dict - 1
            if mag_dict[char] < 0:
                return False
        return True

print(Solution().canConstruct('aa','aab'))
