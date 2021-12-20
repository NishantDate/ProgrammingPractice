class SortedSquares:
    def sortedSquares(self, A):
        result = [None] * len(A)
        l = 0
        r = len(A) - 1
        for index in range(len(A) - 1, -1 , -1):
            if abs(A[l]) > abs(A[r]):
                result[index] = A[l] * A[l]
                l += 1
            else:
                result[index] = A[r] * A[r]
                r -= 1
        return result
            
someSolution = SortedSquares()
nums = [-4,-1,0,3,10]
print(someSolution.sortedSquares(nums))
