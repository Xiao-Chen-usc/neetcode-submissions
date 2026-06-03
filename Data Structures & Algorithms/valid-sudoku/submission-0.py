class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        box = collections.defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] not in row[i] and board[i][j] not in col[j]:
                    if board[i][j] != ".":
                        row[i].add(board[i][j])
                        col[j].add(board[i][j])
                else:
                    return False
                row_box = i//3
                col_box = j//3 
                num_box = 3*row_box + col_box
                if board[i][j] not in box[num_box]:
                    if board[i][j] != ".":
                        box[num_box].add(board[i][j])
                else:
                    return False
        return True

