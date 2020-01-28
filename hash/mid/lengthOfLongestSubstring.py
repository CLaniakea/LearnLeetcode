'''
refer the solution of leetcode
and
https://blog.csdn.net/tangyuan_sibal/article/details/88919612
2nd has some problem!
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = {} # init a dict one val is per character and another is the length of current character the last time of ouucring.
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans
        # if len(s) == 0:
        #     return 1
        # else:
        #     tag = [-1] * 26
        #     i = 0
        #     cur_len = 0
        #     max_len = 0
        #     while i < len(s):
        #         prevIndex = tag[ord(s[i]) - ord('a')]
        #         if prevIndex < 0 or i - prevIndex > cur_len:
        #             cur_len += 1
        #         else:
        #             if cur_len > max_len:
        #                 max_len = cur_len
        #             cur_len = i - prevIndex
        #         tag[ord(s[i]) - ord('a')] = i
        #         if cur_len > max_len:
        #             max_len = cur_len
        #         i += 1
        # return max_len



#print(L[ord('b')-ord('a')])
# ret = Solution()
# print(ret.lengthOfLongestSubstring(" aabcda"))
L = [
  [-1, 0, 1],
  [-1, -1, 2]
]
L.append([1,2,-3])
print(type(L))
print(L)