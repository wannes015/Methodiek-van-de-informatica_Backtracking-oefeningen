#Hierbij enkele handige trucks
CONTINUE = "CONTINUE"
ACCEPT = "ACCEPT"
ABANDON = "ABANDON"


# Hulpfuncties #
################

# Geeft weer of een bepaald punt een kruispunt is (en dus meer dan 2 keer bezocht mag worden)
def is_kruispunt(stratenplan, pos):
    identifier = 0
    DIMENSION = len(stratenplan[0])

    for i in range(2):
        for j in range(2):
            if 0 <= pos[j] - 1 + 2 * i < DIMENSION:
                updated_pos = list(pos)
                updated_pos[j] += -1 + 2 * i

                # Tel 1 op bij "identifier" per aanliggend stuk straat
                if stratenplan[updated_pos[1]][updated_pos[0]] > 0:
                    identifier += 1

    return identifier > 2


# ONDERSTAANDE FUNCTIE KAN GEBRUIKT WORDEN TER OPTIMALISATIE IN DE EXTEND FUNCTIE - NODIG OM HET 11x11 STRATEPLAN OP TE LOSSEN
# ZELF GESCHREVEN OPTIMALISATIES KUNNEN UITERAARD OOK VOLSTAAN

# Geeft True terug als een nieuwe positie efficient is.
# → Onder een niet efficiente move verstaan we willekeurig omkeren zonder dat de huidige positie een bestemming (voor een pakje) is.
def efficient_move(stratenplan, par_sol, latest_pos, updated_pos):
    if len(par_sol) > 1:
        if par_sol[-2] == tuple(updated_pos):
            if stratenplan[latest_pos[1]][latest_pos[0]] == 2:
                return True
            else:
                return False
        else:
            return True
    else:
        return True


def examine(stratenplan, package_count, par_sol):
    latest_pos = par_sol[-1]

    # Nakijken of positie "op de weg" is
    if stratenplan[latest_pos[1]][latest_pos[0]] == 0:
        return ABANDON

    # Als er niet meer dan 2 aanliggende straten zijn hebben we geen knooppunt en mag onze bezorger dit punt maximaal 2 keer bezoeken
    if not is_kruispunt(stratenplan, latest_pos):
        if par_sol.count(latest_pos) > 2:
            return ABANDON
    else:
        if par_sol.count(latest_pos) > 3:
            return ABANDON

    # Count Packages
    delivered_packages = []
    for pos in par_sol:
        if stratenplan[pos[1]][pos[0]] == 2:
            delivered_packages.append(pos)

    if len(set(delivered_packages)) == package_count:
        return ACCEPT

    return CONTINUE



def extend(stratenplan, package_count, par_sol):
    extended = []

    DIMENSION = len(stratenplan[0])
    latest_pos = par_sol[-1]

    for i in range(2):
        for j in range(2):
            if 0 <= latest_pos[j] -1 + 2*i < DIMENSION:
                updated_pos = list(latest_pos)
                updated_pos[j] += -1 + 2*i

                if efficient_move(stratenplan, par_sol, latest_pos, updated_pos):
                    extended.append(par_sol + [tuple(updated_pos)])



    return extended

def solve(stratenplan, package_count, par_sol = [], depth = 0):
    exam = examine(stratenplan, package_count, par_sol)

    results = []

    if exam == ABANDON:
        return None
    if exam == ACCEPT:
        results.append(par_sol)
        return results

    if depth > 121:
        print("Something wrong")

    for p in extend(stratenplan, package_count, par_sol):
        sol = solve(stratenplan, package_count, p, depth + 1)
        if not sol == None:
            results = results + sol

    if depth == 0:
        return min([len(route) for route in results])
    return results

### LITE VERSION
stratenplan = [
    [0, 1, 1, 2, 1, 1],
    [1, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0, 2],
    [0, 1, 0, 2, 1, 1],
    [2, 1, 0, 0, 1, 0],
]
start = (0, 1)
package_count = 4

assert solve(stratenplan, package_count, [start]) == 22

### HARD VERSION - programma moet al enigzins efficient werken om dit op te kunnen lossen (bij mij duurt het een drietal seconden)

# stratenplan = [
#     [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1],
#     [2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
#     [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
#     [0, 1, 0, 1, 0, 2, 0, 0, 1, 0, 0],
#     [0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
#     [0, 1, 0, 0, 0, 1, 1, 1, 1, 2, 1],
#     [0, 2, 0, 1, 0, 1, 0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 0, 1, 1, 1, 2, 0, 1],
#     [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1]
# ]
# package_count = 7
# start = (9, 4)
#
# assert solve(stratenplan, package_count, [start]) == 67