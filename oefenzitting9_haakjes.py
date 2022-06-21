#Hierbij enkele handige trucks
CONTINUE = "CONTINUE"
ACCEPT = "ACCEPT"
ABANDON = "ABANDON"

def examine(data, par_sol):
    # Allereerst alle condities opstellen waarbij de oplossing ongeldig zou zijn en dus ge ABANDONed moet worden
    if len(par_sol) == 0:
        return CONTINUE

    if par_sol[0] == ")":
        return ABANDON

    open_count = 0
    closed_count = 0
    for el in par_sol:
        if el == "(":
            open_count += 1
        else:
            closed_count += 1

        # Closed count can't exceed open count
        if closed_count > open_count:
            return ABANDON
        # Open count can't exceed n
        if open_count > data or closed_count > data:
            return ABANDON

    # Hierna een check uitschrijven die voldoen moet zijn om een geACCEPTeerde oplossing te zijn...
    if len(par_sol) / 2 == data:
        return ACCEPT


    # CONTINUE zou altijd de laatste optie moeten zijn, hiervoor mogen geen checks zijn
    return CONTINUE



def extend(data, par_sol):
    extended = []

    # Hier schrijf je een functie die de oplossingen extend
    extended.append(par_sol + "(")
    extended.append(par_sol + ")")

    return extended

# @param    [data]      bijvoorbeeld een lijst van mogelijke muntstukken, afstanden
#           par_sol     een partiele oplossing
#           depth       ...
#
# @return   - indien er geen geldige route bestaat tussen alle steden in de data-structuur 'afstanden'
#               dan geeft de functie None terug
#           - indien er wel een geldige route bestaat, dat geeft de functie de lengte van de kortste geldige route weer

def solve(data, par_sol = "", depth = 0):
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


oplossingen2 = solve(3)
print(oplossingen2)
# assert set(oplossingen2) == {"((()))", "(()())", "(())()", "()(())", "()()()"}