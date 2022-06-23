#Hierbij enkele handige trucks
CONTINUE = "CONTINUE"
ACCEPT = "ACCEPT"
ABANDON = "ABANDON"

def examine(afstanden, par_sol):
    if len(par_sol) == 0:
        return CONTINUE

    beschikbare_steden = set(
        list(map(lambda route: route[0], afstanden)) + list(map(lambda route: route[1], afstanden)))

    start = par_sol[0][0]
    end = None

    # Check that all cities are only visited once
    for route in par_sol:
        stad = route[1]
        if stad not in beschikbare_steden:
            return ABANDON
        beschikbare_steden.remove(stad)
        end = stad

    if len(beschikbare_steden) == 0 and end == start:
        # Make sure routes are following up
        for i in range(len(par_sol) - 1):
            if not par_sol[i][1] == par_sol[i + 1][0]:
                return ABANDON
        return ACCEPT

    return CONTINUE



def extend(afstanden, par_sol):
    extended = []

    afstanden = list(afstanden) + list(map(lambda route: (route[1], route[0], route[2]), afstanden))
    for route in afstanden:
        extended.append(par_sol + [route])

    return extended

# @param    [data]      bijvoorbeeld een lijst van mogelijke muntstukken, afstanden
#           par_sol     een partiele oplossing
#           depth       ...
#
# @return   - indien er geen geldige route bestaat tussen alle steden in de data-structuur 'afstanden'
#               dan geeft de functie None terug
#           - indien er wel een geldige route bestaat, dat geeft de functie de lengte van de kortste geldige route weer

def solve(afstanden, par_sol = [], depth = 0):
    exam = examine(afstanden, par_sol)

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

    for p in extend(afstanden, par_sol):
        sol = solve(afstanden, p, depth + 1)
        if not sol == None:
            results = results + sol

    if depth == 0:
        if len(afstanden) == 0:
            return 0

        if results == None or len(results) == 0:
            return None
        weglengtes = list(map(lambda optie: sum(afstand for _, _, afstand in optie), results))
        return min(weglengtes)

    return results


afstanden = { ("A", "B", 12), ("A", "C", 24), ("C", "D", 42),
                  ("D", "E", 17), ("E", "A", 9), ("E", "B", 15) }
print(solve(afstanden))
exit()

def main():

    voorbeeld_nr = 1
    # Voorbeeld
    afstanden = { }
    beste_route = solve(afstanden)
    print("Voorbeeld", voorbeeld_nr, ": ", beste_route)
    assert beste_route == 0
    voorbeeld_nr += 1

    # Voorbeeld
    afstanden = { ("A", "B", 2)}
    beste_route = solve(afstanden)
    print("Voorbeeld", voorbeeld_nr, ": ", beste_route)
    assert beste_route == 4
    voorbeeld_nr += 1

    # Voorbeeld
    afstanden = { ("A", "B", 2), ("B", "C", 3)}
    beste_route = solve(afstanden)
    print("Voorbeeld", voorbeeld_nr, ": ", beste_route)
    assert beste_route == None
    voorbeeld_nr += 1

    # Voorbeeld
    afstanden = { ("A", "B", 12), ("A", "C", 24), ("C", "D", 42),
                  ("D", "E", 17), ("E", "A", 9), ("E", "B", 15) }
    beste_route = solve(afstanden)
    print("Voorbeeld", voorbeeld_nr, ": ", beste_route)
    assert beste_route == 110
    voorbeeld_nr += 1

    # Voorbeeld
    afstanden = { ("A", "B", 12), ("A", "C", 24), ("C", "D", 42),
                  ("D", "E", 17), ("E", "A", 9), ("E", "B", 15),
                  ("D", "A", 2) }
    beste_route = solve(afstanden)
    print("Voorbeeld", voorbeeld_nr, ": ", beste_route)
    assert beste_route == 110
    voorbeeld_nr += 1


# WIJZIG NIETS AAN DE LIJNEN HIERONDER
if __name__ == "__main__":
    main()
