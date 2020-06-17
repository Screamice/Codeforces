class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        elif len(needle) > len(haystack):
            return -1
        size = len(needle)
        for index, letter in enumerate(haystack):
            if letter == needle[0] and needle == haystack[index:index+size]:
                return index
        return -1

sol = Solution()
print(sol.strStr("youtube", "bes"))