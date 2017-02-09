#list filled with list of every line in sudoku
row = []
sudoku = open("puzzle1.sudoku", "r")
for line in sudoku:
    line = line.replace(",", "")
    line = line.rstrip()
    line = list(line)
    line = list(map(int, line))
    row.append(line)
print (row)

#geprint als matrix, weet niet of je hier iets mee kan :)

for stukje in row:
    print (stukje)

