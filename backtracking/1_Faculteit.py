"""
Schrijf met behulp van een while-lus een programma dat n! berekent.
Bewijs de correctheid.
"""
import math

n = int(input('Geef een getal: '))

# PRE: n is een natuurlijk getal
assert 0 <= n
assert 1 <= 1 <= n + 1 and 1 == math.factorial(0)
# Beide asserts zijn ok want beide leden in 0 <= n verhogen met 1 levert 1 <= n+1 op
# Het tweede deel van de tweede assert is triviaal aan voldaan
i = 1
assert 1 <= i <= n + 1 and 1 == math.factorial(i-1)

fac = 1

assert 1 <= i <= n + 1 and fac == math.factorial(i-1)
while (i < n + 1):
    assert 1 <= i <= n + 1 and fac == math.factorial(i - 1) and i < n + 1
    fac *= i
    i += 1
    assert 1 <= i <= n + 1 and fac == math.factorial(i - 1)

assert 1 <= i <= n + 1 and fac == math.factorial(i - 1) and not i < n + 1

print(str(n) + '! = ' + str(fac))
