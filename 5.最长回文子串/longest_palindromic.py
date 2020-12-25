class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.maxlen = 0
        self.retstr = ''
        if len(s) < 2:
            return s
        for i in range(len(s)):
            self.__find_palindrome(s, i, i)
            self.__find_palindrome(s, i, i+1)
        return self.retstr


    def __find_palindrome(self, s, j, k):
        while j >= 0 and k < len(s) and s[j] == s[k]:
            j -= 1
            k += 1
        if self.maxlen < k - j + 1:
            self.maxlen = k - j + 1
            self.retstr = s[j+1:k]