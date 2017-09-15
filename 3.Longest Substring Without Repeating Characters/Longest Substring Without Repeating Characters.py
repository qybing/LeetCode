class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        temp=""
        for ch in s:
            if ch in temp:
                count = max(count,len(temp))
                temp = temp[temp.find(ch)+1:]
            temp+=ch
        return max(count,len(temp))
        