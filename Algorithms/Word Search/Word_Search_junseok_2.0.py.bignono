class Solution:
    def exist(self, board, word) -> bool:
        m = len(board)
        n = len(board[0])
        
        self.visited = [[False for _ in range(n)] for __ in range(m)]
        self.board= board
        self.word= word
        self.worddict= {}
        for idx in range(len(word)-1):
            if self.worddict.get(word[idx]):
                if word[idx+1] not in self.worddict[word[idx]]:
                    self.worddict[word[idx]].append(word[idx+1])
            else:
                self.worddict[word[idx]]= []
        if not self.worddict.get(word[-1]):
            self.worddict[word[-1]] = []

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and self.visited[i][j] != True:
                    self.visited[i][j] = True
                    if self.dfs(i,j,0):
                        return True                        
                    self.visited[i][j] = False
        return False

    def dfs(self,i,j,idx):
        if idx == len(self.word)-1:
            return True
        deltai = [-1,0,1,0]
        deltaj = [0,1,0,-1]
        isValuable = False
        for k in range(4):
            newi = i+deltai[k]
            newj = j+deltaj[k]
            if (newi >= 0 and newi < len(self.board) and (newj >= 0 and newj < len(self.board[0])) and not self.visited[newi][newj]):
                if self.board[newi][newj] in self.worddict[self.board[i][j]]: isValuable = True
                if self.board[newi][newj]==self.word[idx+1]:
                    self.visited[newi][newj] = True
                    if self.dfs(newi,newj,idx+1):
                        return True                    
                    self.visited[newi][newj] = False
        if isValuable:
            self.visited[i][j] =True
a = Solution()