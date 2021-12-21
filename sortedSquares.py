class Solution:
    def sortedSquares(self, A):
        result = [None] * len(A)
        l = 0
        r = len(A) - 1
        for i in range(0, len(A)):
            print(result)
            if (abs(A[r]) > abs(A[l])):
                result[len(A) - i - 1] = A[r] ** 2
                r -= 1
            else:
                print("SWITCH!")
                result[len(A) - i - 1] = A[l] ** 2
                l += 1
        return result

newSolution = Solution()
A = [-4,-1,0,3,10]
print(newSolution.sortedSquares(A))