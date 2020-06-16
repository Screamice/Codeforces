import time
import sys

sys.setrecursionlimit(20000)

class Complexity:

    def factorial_recursivo(self, N):
        if N==0 or N==1:
            return 1
        else:
            return N * self.factorial_recursivo(N-1)

    def factorial_iterativo(self, A):
        answer = 1

        while A > 1:
            answer *= A
            A -= 1
        
        return answer


NUMBER = 10000
obj = Complexity()

start = time.time()
obj.factorial_recursivo(NUMBER)
final = time.time()
print(final-start)


start = time.time()
obj.factorial_iterativo(NUMBER)
final = time.time()
print(final-start)
