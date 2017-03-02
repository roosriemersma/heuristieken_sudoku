RANGE = 9
BOX_RANGE = 3
FIRST_LINE = 2
SECOND_LINE = 5
FIRST = 1
LAST = 10
NULWAARDE = 0

#list filled with list of every line in sudoku
sudoku = []
puzzle = open("puzzle1.sudoku", "r")
for line in puzzle:
    line = line.replace(",", "")
    line = line.rstrip()
    line = list(line)
    line = list(map(int, line))
    sudoku.append(line)

#printen van de sudoku
def sudoku_printen(input):
    for i in range(RANGE):
        for j in range(RANGE):
            if j == FIRST_LINE:
                print (input[i][j], "|", end=" ")
            elif j == SECOND_LINE:
                print(input[i][j], "|", end=" ")
            else:
                print (input[i][j], end=" ")
        print ('\n', end="")
        if i == FIRST_LINE or i == SECOND_LINE:
            print("- - - + - - - + - - -")

#zoeken naar lege plek in sudoku
def zoek_lege_plek(input, plek):

    for rij in range(RANGE):
        for kolom in range(RANGE):
            if(input[rij][kolom] == 0):
                plek[0] = rij
                plek[1] = kolom
                return True
    return False
#nu hebben we de "coordinaten" van een lege plek in de list plek, die we later weer gaan gebruiken

#zoeken of nummer gebruikt wordt in de rij, als nummer in rij zit dan return True
def zit_in_rij(input, rij, nummer):
    for i in range(RANGE):
        if (input[rij][i] == nummer):
            return True
    return False

#zoeken of nummer wordt gebruikt in kolom, als nummer in kolom zit dan return True
def zit_in_kolom(input, kolom, nummer):
    for i in range (RANGE):
        if (input[i][kolom] == nummer):
            return True
    return False

#zoeken of nummer wordt gebruikt in box, als nummer in box zit dan return True
def zit_in_box(input, rij, kolom, nummer):
    for i in range (BOX_RANGE):
        for j in range(BOX_RANGE):
            if (input[i + rij][j + kolom] == nummer):
                return True
    return False

#kijken of nummer op de locatie kan, return een boolean om te kijken of nummer op locatie past
def kan_nummer_hier(input, rij, kolom, nummer):
    return not zit_in_rij(input, rij, nummer) and not zit_in_kolom(input, kolom, nummer) and not zit_in_box(input,rij - rij%BOX_RANGE,kolom - kolom%BOX_RANGE,nummer)

#sudoku oplossen
def sudoku_oplossen(input):
    plek = [NULWAARDE, NULWAARDE]
    if (not zoek_lege_plek(input, plek)):
        return True

    rij = plek[NULWAARDE]
    kolom = plek[1]

    for nummer in range(FIRST, LAST):
        if(kan_nummer_hier(input, rij, kolom, nummer)):
            input[rij][kolom] = nummer
            if (sudoku_oplossen(input)):
                return True
            input[rij][kolom] = NULWAARDE
    return False


if (sudoku_oplossen(sudoku)):
    sudoku_printen(sudoku)
else:
    print ("Geen oplossing mogelijk")
