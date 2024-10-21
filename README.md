# Projet Streamlit - Visualisation des Données du Titanic

## Description
Ce projet est une application interactive développée avec **Streamlit** qui permet de visualiser et d'analyser le célèbre jeu de données du Titanic. Les utilisateurs peuvent interagir avec les données, appliquer des filtres, et télécharger les résultats.

## Fonctionnalités
- **Affichage des données du Titanic** : Visualisation des données complètes et filtrées.
- **Visualisations** : Graphiques interactifs avec Matplotlib, Seaborn et Plotly.
- **Filtres** : Filtrer les données par sexe, classe, et autres critères.
- **Téléchargement de fichiers** : Possibilité de télécharger un fichier CSV contenant les données filtrées.
- **Gestion des fichiers** : Chargement de fichiers CSV depuis l'interface.

## Installation

1. Clonez le projet sur votre machine locale :
    ```bash
    git clone https://github.com/ABOY-IA/streamlit_project.git
    ```

2. Accédez au dossier du projet :
    ```bash
    cd streamlit_project
    ```

3. Installez les dépendances nécessaires :
    ```bash
    pip install -r requirements.txt
    ```

4. Lancez l'application Streamlit :
    ```bash
    streamlit run hello.py
    ```

## Configuration du Thème
L'application utilise un thème personnalisé, défini dans le fichier `.streamlit/config.toml`. Vous pouvez modifier les couleurs et la police selon vos préférences.

Exemple de configuration de thème :

```toml
[theme]
primaryColor = "#000000"  # Couleur principale noire
backgroundColor = "#800080"  # Arrière-plan violet foncé
secondaryBackgroundColor = "#FFFFFF"  # Arrière-plan secondaire blanc
textColor = "#000000"  # Texte en noir
font = "sans serif"  # Police sans serif
```

## Utilisation
- L'interface principale permet de :
  - Visualiser les données du Titanic.
  - Appliquer des filtres (par sexe, classe, etc.).
  - Visualiser des graphiques interactifs.
  - Télécharger les résultats filtrés sous forme de fichier CSV.

- **Instructions pour l'utilisation :**
  1. Ouvrez l'application Streamlit via la commande :
     ```bash
     streamlit run hello.py
     ```
  2. Interagissez avec les widgets (boutons, curseurs, sélecteurs déroulants) pour explorer les données.
  3. Visualisez les graphiques générés dynamiquement à partir des données filtrées.
  4. Téléchargez les données filtrées en cliquant sur le bouton de téléchargement.

## Tests
Pour exécuter les tests unitaires, utilisez la commande suivante :

```bash
pytest
```
Cette commande exécutera tous les tests définis dans les fichiers test_*.py de votre projet. Assurez-vous que Pytest est installé dans votre environnement virtuel

## Technologies Utilisées
- **Streamlit** : Pour l'interface utilisateur interactive.
- **Pandas** : Pour la manipulation des données.
- **Matplotlib** : Pour les visualisations de données avec des graphiques statiques.
- **Seaborn** : Pour les visualisations avancées des données.
- **Plotly** : Pour les visualisations interactives des données.
- **Pytest** : Pour les tests unitaires.

## Auteur
- **KaRn1zC**

## Licence
Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus d'informations.
