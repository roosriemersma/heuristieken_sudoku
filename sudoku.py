rows = []
row = []
sudoku = open("puzzle1.sudoku", "r")
for line in sudoku:
    line = line.replace(",", "")
    line = line.rstrip()
    line = list(line)
    line = list(map(int, line))
    row.append(line)
#row = list(map(int, row))
print (row)
