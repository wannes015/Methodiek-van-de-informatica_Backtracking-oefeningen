CONTINUE = "CONTINUE"
ACCEPT = "ACCEPT"
ABANDON = "ABANDON"

# SPELREGELS
##########################
# 1. De speler kan enkel naar aanliggende posities gaan (niet schuin)
# 2. De speler moet binnen de muren van het doolhof blijven (enkel vakjes met 1 zijn toegelaten)
# 3. Het doolhof is altijd eenvoudig kubisch (jaja, juist materiaalkunde gehad gy weet)
# 4. Elke positie mag maar 1 keer bezocht worden

# Doel: bepaal de lengte van het kortst mogelijke pad

def examine(maze, end, par_sol):
    # Checken of laatste positie valid is (geen muur)
    latest_pos = par_sol[-1]
    if not maze[latest_pos[0]][latest_pos[1]][latest_pos[2]] == 1:
        return ABANDON

    # Checken of laatste positie niet al eens is geweest
    if par_sol.count(latest_pos) > 1:
        return ABANDON

    if latest_pos == end:
        return ACCEPT

    return CONTINUE



def extend(maze, end, par_sol):
    extended = []

    DIMENSION = len(maze[0][0])
    latest_pos = par_sol[-1]

    for i in range(2):
        for j in range(3):
            if 0 <= latest_pos[j] -1 + 2*i < DIMENSION:
                new_pos = list(latest_pos)
                new_pos[j] += -1 + 2*i

                extended.append(par_sol + [tuple(new_pos)])

    return extended


def solve(maze, end, par_sol = [], depth = 0):
    exam = examine(maze, end, par_sol)

    results = []

    if exam == ABANDON:
        return None
    if exam == ACCEPT:
        results.append(par_sol)
        return results


    for p in extend(maze, end, par_sol):
        sol = solve(maze, end, p, depth + 1)
        if not sol == None:
            results = results + sol

    if depth > 0:
        return results

    return min([len(path) for path in results])




start = (3, 3, 0)
end = (0, 0, 3)

maze = [
    [
        [0, 0, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0],
    ],
    [
        [0, 1, 1, 0],
        [0, 1, 0, 1],
        [0, 0, 1, 1],
        [0, 0, 1, 0],
    ],
    [
        [1, 0, 1, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
    ],
    [
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [1, 1, 1, 1],
        [1, 0, 0, 0],
    ],
]

assert solve(maze, end, [start]) == 10,  "Incorrecte lengte"