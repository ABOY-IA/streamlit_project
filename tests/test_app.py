import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
import pandas as pd
from io import StringIO

# Exemple de fonction que nous voulons tester
def charger_donnees(fichier):
    return pd.read_csv(fichier)

# Test pour la fonction 'charger_donnees'
def test_charger_donnees():
    # Simuler un fichier CSV
    fichier_csv = StringIO("Name,Age,Sex\nJohn,28,Male\nAlice,24,Female")
    
    # Charger les données
    data = charger_donnees(fichier_csv)
    
    # Vérifier que les données sont bien chargées
    assert not data.empty  # Vérifie que le DataFrame n'est pas vide
    assert list(data.columns) == ["Name", "Age", "Sex"]  # Vérifie les colonnes
    assert len(data) == 2  # Vérifie qu'il y a deux lignes

# Test pour vérifier que le fichier CSV manquant est géré correctement
def test_fichier_inexistant():
    with pytest.raises(FileNotFoundError):
        charger_donnees("fichier_inexistant.csv")
