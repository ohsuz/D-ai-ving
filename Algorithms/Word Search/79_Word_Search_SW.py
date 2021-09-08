class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r, c = len(board), len(board[0])
        
        move = [(1,0),(0,-1),(0,1),(-1,0)]
        checked = [[False for _ in range(c)] for _ in range(r)]
        flag = False
        
        def dfs(row, col, now_word_idx):    
            nonlocal checked
            nonlocal flag
            
            if not flag and board[row][col] == word[now_word_idx] and not checked[row][col]:
                
                if now_word_idx == len(word) - 1 :
                    flag = True
                
                else:
                    checked[row][col] = True
                    for m in move:
                        if 0 <= row + m[0] < r and 0 <= col + m[1] < c:
                            dfs(row+m[0],col+m[1], now_word_idx+1)
                    checked[row][col] = False
        
        for i in range(r):
            for j in range(c):
                dfs(i,j,0)
        
        return flag