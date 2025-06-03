"""
Vérifier si un tableau est un palindrome
"""

def est_palindrome(tableau):
    return tableau == tableau[::-1]


tableau = [1, 2, 3, 2, 1]
if est_palindrome(tableau):
    print("Le tableau est un palindrome.")
else:
    print("Le tableau n'est pas un palindrome.")
