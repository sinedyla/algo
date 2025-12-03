#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Programme de bienvenue simple
Un premier programme pour apprendre les bases de Python
"""

def dire_bonjour():
    """Affiche un message de bienvenue"""
    print("Bonjour ! 👋")
    print("Bienvenue dans ce dépôt d'apprentissage d'algorithmes !")
    print("Hello! Welcome to this algorithm learning repository!")

def dire_bonjour_personnalise(nom):
    """Affiche un message de bienvenue personnalisé
    
    Args:
        nom (str): Le nom de la personne à saluer
    """
    print(f"Bonjour {nom} ! 👋")
    print(f"Ravi de vous voir ici !")

if __name__ == "__main__":
    # Message de bienvenue simple
    dire_bonjour()
    print()
    
    # Demander le nom de l'utilisateur
    nom = input("Comment vous appelez-vous ? ")
    if nom:
        print()
        dire_bonjour_personnalise(nom)
