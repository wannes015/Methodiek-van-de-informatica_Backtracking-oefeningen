####################################################
# Tutorial toegepast op de sudoku (oefenzitting 9) #
####################################################

##################
# Print functies #
##################
from copy import deepcopy

def print_rij(rij):
    for nummer in rij:
        print("|", nummer, end=" ")
    print("|")


def print_bord(bord):
    print("*---" * len(bord), "*", sep="")
    for rij in bord:
        print_rij(rij)
        print("*---" * len(bord), "*", sep="")



#Hierbij enkele handige trucks
CONTINUE = "CONTINUE"
ACCEPT = "ACCEPT"
ABANDON = "ABANDON"


# Helper function
def get_columns(sudoku):
    # assume sudoku is square (9x9)
    columns = []
    for i in range(9):
        columns.append([])
        for j in range(9):
            columns[i].append(sudoku[j][i])

    return columns


def get_squares(sudoku):
    # sudoku bestaat uit 3x3 gebied van 3x3 vierkanten
    # sq1 sq2 sq3
    # sq4 sq5 sq6
    # sq7 sq8 sq9

    squares = []
    for sq_horizontal_co in range(3):
        for sq_vertical_co in range(3):
            squares.append([])
            for i in range(3 * sq_horizontal_co, 3 * (sq_horizontal_co + 1)):
                for j in range(3 * sq_vertical_co, 3 * (sq_vertical_co + 1)):
                    squares[-1].append(sudoku[i][j])

    return squares


def is_valid(data):
    for row in data:
        checked_numbers = set()
        for number in row:
            if number in checked_numbers and number != 0:
                return False

            checked_numbers.add(number)

    return True


def examine(data, par_sol):
    # Allereerst alle condities opstellen waarbij de oplossing ongeldig zou zijn en dus ge ABANDONed moet worden

    # 1: RIJEN CHECKEN (ABANDON ALS EEN GETAL (verschillend van 0) MEER DAN EEN KEER VOORKOMT)
    if not is_valid(par_sol):
        return ABANDON

    # 2: KOLOMMEN CHECKEN
    if not is_valid(get_columns(par_sol)):
        return ABANDON

    # 3x3 VIERKANTEN CHECKEN
    if not is_valid(get_squares(par_sol)):
        return ABANDON

    # Hierna een check uitschrijven die voldoen moet zijn om een geACCEPTeerde oplossing te zijn...
    if sum(row.count(0) for row in par_sol) == 0:
        return ACCEPT

    # CONTINUE zou altijd de laatste optie moeten zijn, hiervoor mogen geen checks zijn
    return CONTINUE



def extend(data, par_sol):
    extended = []

    # Hier schrijf je een functie die de oplossingen extend
    for y_idx, row in enumerate(par_sol):
        for x_idx, number in enumerate(row):
            if number == 0:
                for new_num in range(9):
                    extended.append(deepcopy(par_sol))
                    extended[-1][y_idx][x_idx] = new_num + 1
                break
        else:
            continue
        break

    return extended

# @param    [data]      bijvoorbeeld een lijst van mogelijke muntstukken, afstanden
#           par_sol     een partiele oplossing
#           depth       ...
#
# @return   - indien er geen geldige route bestaat tussen alle steden in de data-structuur 'afstanden'
#               dan geeft de functie None terug
#           - indien er wel een geldige route bestaat, dat geeft de functie de lengte van de kortste geldige route weer

def solve(data, par_sol = [], depth = 0):
    exam = examine(data, par_sol)

    results = []

    # Onderstaande functie kan gebruikt worden om niet dieper dan "n" (in dit geval 2) iteraties te gaan, kan handig
    # zijn wanneer je moet testen met data die voor veel iteraties zorgt.

    # if depth > 2:
    #     return None

    if exam == ABANDON:
        return None
    if exam == ACCEPT:
        results.append(par_sol)
        return results


    for p in extend(data, par_sol):
        sol = solve(data, p, depth + 1)
        if not sol == None:
            results = results + sol

    return results


b4 = [[0, 3, 4, 6, 7, 8, 9, 1, 0],
      [6, 0, 2, 1, 9, 5, 3, 0, 8],
      [1, 9, 0, 3, 4, 2, 0, 6, 7],
      [8, 5, 9, 0, 6, 0, 4, 2, 3],
      [4, 2, 6, 8, 0, 3, 7, 9, 1],
      [7, 1, 3, 0, 2, 0, 8, 5, 6],
      [9, 6, 0, 5, 3, 7, 0, 8, 4],
      [2, 0, 7, 4, 1, 9, 6, 0, 5],
      [0, 4, 5, 2, 8, 6, 1, 7, 0]]

# We geven de sudoku mee als partial solution omdat we anders een default waarde voor par_sol moeten voorzien die aan een 9x9 sudoku gelijkt...
print(solve(b4, b4))

