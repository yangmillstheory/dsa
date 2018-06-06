class Solution:
    def isPalindrome(self, string):
        n = len(string)
        i, j = 0, n-1
        while True:
            while i < n and not string[i].isalnum():
                i += 1
            while j >= 0 and not string[j].isalnum():
                j -= 1
            if i > j or i > n or j < 0:
                break
            elif string[i].lower() != string[j].lower():
                return False
            i += 1
            j -= 1
        return True
