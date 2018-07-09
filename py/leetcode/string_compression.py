TERM = '-'


class Solution(object):
    def compress(self, chars):
        '''Run-length compression on a list of characters in O(n) time and O(1) space.'''
        i = count = 0
        chars.append(TERM)
        for j, ch in enumerate(chars):
            if j == 0 or ch == chars[j-1]:
                count += 1
            else:
                chars[i] = chars[j-1]
                i += 1
                if count > 1:
                    for d in str(count):
                        chars[i] = d
                        i += 1
                count = 1
        chars.pop()
        return i
