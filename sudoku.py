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

#printen van de sudoku
def print_sudoku(input):
    for i in range(9):
        for j in range(9):
            print (x[i][j]),
        print ('\n')

#zoeken naar lege plek in sudoku
def zoek_lege_plek(input, plek):
    for rij in range(9):
        for kolom in range(9):
            if(input[rij][kolom] == 0):
                plek[0] = rij
                plek[1] = kolom
                return True
    return False
#nu hebben we de "coordinaten" van een lege plek in de list plek, waarmee we nu verder gaan werken


#zoeken of nummer gebruikt wordt in de rij, als nummer in rij zit dan return True
def zit_in_rij(intput, rij, nummer):
    for i in range(9):
        if (input[rij][i] == nummer):
            return True
    return False

#zoeken of nummer wordt gebruikt in kolom, als nummer in kolom zit dan return True
def zit_in_kolom(input, kolom, nummer):
    for i in range (9):
        if (input[i][kolom] == nummer):
            return True
    return False

#zoeken of nummer wordt gebruikt in box, als nummer in box zit dan return True
def zit_in_box(input, rij, kolom, nummer):
    for i in range (3)
        for j in range(3)
            if (input[i + rij][j + kolom] == nummer):
                return True
    return False

