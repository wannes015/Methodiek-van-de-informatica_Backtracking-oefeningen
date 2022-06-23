##########################
#   POST-NL    PLANNER   #
##########################

# Visuele ondersteuning: https://github.com/wannes015/mi_examen/blob/master/postnl_planner_stratenplan.jpg
# Oplossing zie : https://github.com/wannes015/mi_examen


# Yay, na 5 jaar zwoegen bent ge eindelijk afgestudeerd als volwaardige burgie.
# Na veel zoeken naar een toffe job komt ge uiteindelijk terecht bij PostNL. (basically de postduif van BOL.com)
# Je job bestaat uit het ontwikkelen van een programma dat een optimale route voor jouw chauffeurs zoekt.
# Je moet dus, gegeven een straatplan, de kortste route zoeken zodat alle pakketjes geleverd kunnen worden. Hiertoe
# zijn wel enkele voorwaarden.

# Voorwaarden:
# 1. Een chauffeur niet meer dan twee keer door de zelfde straat rijden (elke positie mag max 2 keer voorkomen in de optimale route)
# 2. Een uitzondering op regel 1 zijn zogenaamde kruispunten. Hieronder verstaan we punten waarop wegen samenkomen. Deze mag hij maximaal 3 keer bezoeken.
# 3. Een chauffeur zijn route stopt op de moment dat het laatste pakketje is afgeleverd (daarna caren we niet meer [en betalen we evenmin hehe {based on true stories}])

# Gegevens
# 1. straatplan (nxn matrix)
#       LEGENDE:
#           0. Dit is terrein waar de chauffeur niet mag komen (aka geen straat)
#           1. Dit is "baan" waarover de chauffeur mag rijden
#           2. Dit zijn bestemmingen waar een pakje afgeleverd moet worden
#
# 2. package_count: geeft weer hoeveel pakketjes er in totaal moeten afgeleverd worden
# 3. start: geeft de locatie van het depot weer, vanaf hier vertrekt de chauffeur uiteraard.


CONTINUE = "CONTINUE"
ACCEPT = "ACCEPT"
ABANDON = "ABANDON"

################
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
    # TIP: gebruikt de functie is kruispunt om te checken of een positie al dan niet meer dan 2 keer mag voorkomen
    # (Uiteraard beter als je dit niet gebruikt en zelf iets verzint)
    pass



def extend(stratenplan, package_count, par_sol):
    extended = []

    # ONDERSTAANDE FUNCTIE KAN GEBRUIKT WORDEN TER OPTIMALISATIE, MAAR IS ZEKER NIET NODIG OM HET 6x6 STRATENPLAN OP TE LOSSEN,
    # ANDERE FUNCTIES ZIJN OOK ZEKER MOGELIJK TER OPTIMALISATIE, DIT IS GEWOON WAT IK HEB GEBRUIKT
    # if efficient_move(stratenplan, par_sol, old_pos, new_pos):

    return extended


def solve(stratenplan, package_count, par_sol = [], depth = 0):
    pass

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