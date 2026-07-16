# 79. Word Search

# Medium

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

# Example 1:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
 

# Constraints:

# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLUMNS = len(board), len(board[0])
        visited = set()

        def dfs(r,c,i):
            if i == len(word):
                return True
            
            if (r<0 or c<0 or
                r>= ROWS or c >= COLUMNS or
                (r,c) in visited or
                word[i] != board[r][c]):
                return False
            
            visited.add((r,c))
            res = (dfs(r+1,c,i+1) or
                    dfs(r-1,c,i+1) or
                    dfs(r,c+1,i+1) or 
                    dfs(r,c-1,i+1))
            visited.remove((r,c))
            return res

        for r in range(ROWS):
            for c in range(COLUMNS):
                if dfs(r,c,0):
                    return True
                
        return False
    

# Recursion and Backtracking solution
# We can use recursion and backtracking to explore all possible paths in the grid to find the word.
# The dfs function takes the current row r, column c, and index i of the word as arguments.
# If the index i equals the length of the word, we have found the word and return True.
# If the current cell is out of bounds, already visited, or does not match the current character of the word, we return False.
# We mark the current cell as visited and recursively explore the neighboring cells (up, down, left, right) to find the next character of the word.
# After exploring all possible paths, we backtrack by unmarking the current cell as visited.
# We call the dfs function for each cell in the grid to check if the word can be found starting from that cell.
# Time complexity is O(N * 4^L), where N is the number of cells in the grid and L is the length of the word. 
# In the worst case, we may explore all possible paths for each cell.
# Space complexity is O(L) for the recursion stack, where L is the length of the word.