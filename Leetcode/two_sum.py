class Solution:

    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype answer: List[int]
        """
        answer = []
        first, last = 0, len(numbers)-1
        while first < last:
            sum = numbers[first] + numbers[last]
            print(f"first vale {first} y las vale {last}")
            if target > sum:
                first += 1
                print(f"Ahora first vale {first}")
            elif target < sum:
                last -= 1
                print(f"Ahora last vale {last}")
            if target == sum:
                answer.append(first+1)
                answer.append(last+1)
                break
        
        return answer

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))