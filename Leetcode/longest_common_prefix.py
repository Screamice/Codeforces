class Solution:
    def longestCommonPrefix(self, strs):
        aux = []
        for c in strs:
            aux.append(len(c))
        size = min(aux)

        for i in range(size-1):
            if strs[0][i] == strs[1][i] == strs[2][i]:
                prefix += strs[0][i]
        
        return size

sol = Solution()
print(sol.longestCommonPrefix(["flower","flows","flight"]))