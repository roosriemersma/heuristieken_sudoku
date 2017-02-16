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
def sudoku_printen(input):
    for i in range(9):
        for j in range(9):
            print (input[i][j]),
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
#nu hebben we de "coordinaten" van een lege plek in de list plek, die we later weer gaan gebruiken


#zoeken of nummer gebruikt wordt in de rij, als nummer in rij zit dan return True
def zit_in_rij(input, rij, nummer):
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
    for i in range (3):
        for j in range(3):
            if (input[i + rij][j + kolom] == nummer):
                return True
    return False

#kijken of nummer op de locatie kan, return een boolean om te kijken of nummer op locatie past
def kan_nummer_hier(input, rij, kolom, nummer):
    return not zit_in_rij(input, rij, nummer) and not zit_in_kolom(input, kolom, nummer) and not zit_in_box(input,rij - rij%3,kolom - kolom%3,nummer)

#sudoku oplossen
def sudoku_oplossen(input):
    plek = [0, 0]
    if (not zoek_lege_plek(input, plek)):
        return True

    rij = plek[0]
    kolom = plek[1]

    for nummer in range(1, 10):
        if(kan_nummer_hier(input, rij, kolom, nummer)):
            input[rij][kolom] = nummer
            if (sudoku_oplossen(input)):
                return True
            input[rij][kolom] = 0
    return False


if (sudoku_oplossen(sudoku)):
    sudoku_printen(sudoku)
else:
    print ("Geen oploossing mogelijk")
