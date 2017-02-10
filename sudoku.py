#list filled with list of every line in sudoku
sudoku = []
puzzle = open("puzzle1.sudoku", "r")
for line in puzzle:
    line = line.replace(",", "")
    line = line.rstrip()
    line = list(line)
    line = list(map(int, line))
    sudoku.append(line)
print (sudoku)

#geprint als matrix, weet niet of je hier iets mee kan :)

for row in sudoku:
    print (row)

#kolom geprint, waat ook niet of we hier iets mee kunnen, loop maken lukt me niet
for firstNumb in sudoku:
    print (firstNumb[0:1])
