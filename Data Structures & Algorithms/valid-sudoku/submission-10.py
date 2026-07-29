class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {}
        col = {}
        box = {}
        for i in range(9):
            for j in range(9):
                value = board[i][j]
                box_key = (i//3) * 3 + (j//3)
                if value == ".":
                    continue
                if i not in row:
                    row[i] = set()
                if j not in col:
                    col[j] = set()
                if box_key not in box:
                    box[box_key] = set()
                if value in row[i] or value in col[j] or value in box[box_key]:
                    return False

                row[i].add(value)
                col[j].add(value)
                box[box_key].add(value)
                    
        return True
                