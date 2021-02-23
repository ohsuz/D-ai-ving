class Solution:
    def constrainedSubsetSum(self, nums, k: int) -> int:
        limit, result, minuses, maxVal = k-1, -1, [], -1
        for num in nums:
            if num >= 0:
                if len(minuses) > k-1:
                    result += self.dp(minuses, limit)     
                minuses = []
                result = num if num > result+num else result + num
                maxVal = result if result > maxVal else maxVal  
            else:
                minuses.append(num)
        return maxVal 
    
    def dp(self, minuses, limit):
        if limit == 0:
            return sum(minuses)
        dpgraph = [[0,0] for _ in minuses]
        dpgraph[0][1] = minuses[0]
        for i in range(1,len(dpgraph)):
            dpgraph[i][0] = max([dp[1] for dp in dpgraph[i-limit:i]]) if i-limit>=0 else 0
            dpgraph[i][1] = (dpgraph[i-1][0] if dpgraph[i-1][0] > dpgraph[i-1][1] else dpgraph[i-1][1]) + minuses[i]
        return dpgraph[-1][0] if dpgraph[-1][0] > dpgraph[-1][1] else dpgraph[-1][1]

a = Solution()
print(a.constrainedSubsetSum([10,2,-10,5,20],2))
print(a.constrainedSubsetSum([-1,-2,-3],1))
print(a.constrainedSubsetSum([10,-2,-10,-5,20],2))
print(a.constrainedSubsetSum([1],2))
print(a.constrainedSubsetSum([-1],2))
print(a.constrainedSubsetSum([1,-10,-10,-1,-10,-10,-1,-10,-10,-10,1],4))
print(a.constrainedSubsetSum([1,-10,-10,-1,-10,-10,-1,-10,-10,-10,1],3))
print(a.constrainedSubsetSum([-5266,4019,7336,-3681,-5767],2)) # 11355
print(a.constrainedSubsetSum([-8269,3217,-4023,-4138,-683,6455,-3621,9242,4015,-3790],1)) # 16091
print(a.constrainedSubsetSum([100,-10,-10,-10,-2,-2,-10,-100,15,-5,-10,10,2,-10,5,20],2)) # 125
print(a.constrainedSubsetSum([3,-1,-1,-1,-1,-1,-1,-1,15,-1,-1,-1,12],5)) # 29