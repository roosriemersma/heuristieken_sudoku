rows = []
sudoku = open("puzzle1.sudoku", "r")
for line in sudoku:
    line = line.replace(",", "")
    #list(line)
    rows.append(line.rstrip())
print (rows)