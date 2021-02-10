class Solution:
    def constrainedSubsetSum(self, nums, k: int) -> int:
        limit, result, isEmpty, minuses = k-1, 0, True, []
        for num in nums:
            if num >= 0:
                isEmpty = False
                if len(minuses) > k-1:
                    result += self.dp(minuses, limit)                
                result = 0 if result < 0 else result
                result += num
                minuses = []
            else:
                minuses.append(num)
        if isEmpty:
            result = max(nums)
        return result
    
    def dp(self, minuses, limit):
        result, beforeVal, skip  = 0, 0, 0
        if limit == 0:
            return sum(minuses)
        for minus in minuses:
            if skip != limit:
                skip += 1
            elif  beforeVal > minus:
                result += beforeVal
                skip = 1
            else:
                result += minus
                skip = 0
            beforeVal = minus        
        return result

a = Solution()
# print(a.constrainedSubsetSum([10,2,-10,5,20],2))
# print(a.constrainedSubsetSum([-1,-2,-3],1))
# print(a.constrainedSubsetSum([10,-2,-10,-5,20],2))
# print(a.constrainedSubsetSum([1],2))
# print(a.constrainedSubsetSum([-1],2))
# print(a.constrainedSubsetSum([1,-10,-10,-1,-10,-10,-1,-10,-10,-10,1],4))
# print(a.constrainedSubsetSum([1,-10,-10,-1,-10,-10,-1,-10,-10,-10,1],3))
# print(a.constrainedSubsetSum([-5266,4019,7336,-3681,-5767],2)) # 11355
# print(a.constrainedSubsetSum([-8269,3217,-4023,-4138,-683,6455,-3621,9242,4015,-3790],1)) # 16091
print(a.constrainedSubsetSum([100,-10,-10,-10,-2,-2,-10,-100,15,-5,-10,10,2,-10,5,20],2)) # 125