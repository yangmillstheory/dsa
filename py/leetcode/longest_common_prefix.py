class Solution(object):
    def longestCommonPrefix(self, strings):
        if not strings:
            return ''
        longest = strings[0]
        for i in range(1, len(strings)):
            k = 0
            current = strings[i]
            while k < min(len(current), len(longest)):
                if current[k] != longest[k]:
                    break
                k += 1
            longest = longest[:k]
        return longest
