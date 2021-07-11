from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sorted_citation = sorted(citations, reverse = True)
        h = 0; i = 0; n = len(citations)
        while i < n and sorted_citation[i] > h:
            h += 1
            i += 1
        return h


tag = Solution()
# citations = [3,0,6,1,5]
citations = [1,2,3,4,5,6]

print(tag.hIndex(citations))