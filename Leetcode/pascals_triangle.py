from math import factorial

class Solution:

    def generate(self, rows):
        answer = []
        for n in range(rows):
            aux = []
            for k in range(n+1):
                aux.append(self.coefficient(n,k))
            answer.append(aux)
        
        return answer

    def coefficient(self, n, k):
        return (int)(factorial(n) / (factorial(k) * factorial(n-k)))


sol = Solution()
print(sol.generate(5))