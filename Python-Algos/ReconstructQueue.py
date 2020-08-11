# Suppose you have a random list of people standing in a queue. Each person is described 
# by a pair of integers (h, k), where h is the height of the person and k is the
# number of people in front of this person who have a height greater than equal to h.
# Write an algorithm to reconstruct the queue.

class Solution: 
    def reconstructQueue(self, people):
        people.sort(key=lambda x: (-x[0], x[1])) # O(nLogn)
        res = []
        for p in people: # O(n)
            res.insert(p[1], p) # O(n)
        return res

# Time Complexity: O(n^2)
# Space Complexity: O(n)

print(Solution().reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))