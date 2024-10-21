"""
Version initiale en suivant l'ordre des questions
"""

# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import plotly.express as px
# import logging

# # Titre et en-têtes
# st.title("Hello, Streamlit !")
# st.header("Dataset du Titanic")
# st.subheader("Découverte de streamlit avec ce dataset")

# # Texte explicatif
# st.write("Utilisation de streamlit avec des données en rapport avec le Titanic")
# st.markdown("**Ceci** est réalisé dans le cadre de ma formation chez [Simplon](https://simplon.co)")

# # Titre
# st.header("Affichage des données du Titanic")

# # Charger les données avec gestion des erreurs
# try:
#     data = pd.read_csv("test.csv")
    
#     # Afficher un aperçu des premières lignes
#     st.subheader("Aperçu des premières lignes")
#     st.write(data.head())
    
#     # Affichage interactif du DataFrame complet
#     st.subheader("Affichage interactif du DataFrame")
#     st.dataframe(data)
    
#     # Affichage statique du DataFrame
#     st.subheader("Affichage statique du DataFrame")
#     st.table(data)
    
# except FileNotFoundError:
#     st.error("Le fichier CSV est introuvable. Assurez-vous que le fichier est au bon endroit.")

# # Section Widgets Interactifs
# st.header("Widgets interactifs")

# # Créer un bouton
# if st.button("Cliquez ici"):
#     st.write("Le bouton a été cliqué!")

# # Créer une case à cocher
# if st.checkbox("Afficher les données complètes"):
#     st.write(data)

# # Créer un champ de saisie de texte
# nom_utilisateur = st.text_input("Entrez votre nom")
# st.write(f"Bonjour, {nom_utilisateur}.")

# # Créer un sélecteur déroulant pour choisir une colonne à afficher
# colonne = st.selectbox("Choisissez une colonne à afficher", data.columns)
# st.write(f"Vous avez sélectionné la colonne : {colonne}")
# st.write(data[colonne].head())

# # Créer un curseur pour choisir le nombre de lignes à afficher
# nb_lignes = st.slider("Choisissez le nombre de lignes à afficher", 1, len(data), 5)
# st.write(data.head(nb_lignes))

# # Mise en page avec colonnes
# col1, col2 = st.columns(2)

# with col1:
#     st.write("Colonne 1")
#     st.dataframe(data)

# with col2:
#     st.write("Colonne 2")
#     st.table(data)

# # Mise en page avec un conteneur extensible
# with st.expander("Cliquez ici pour afficher les statistiques descriptives"):
#     st.write(data.describe())

# # Mise en page avec des onglets
# tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

# with tab1:
#     st.write("Contenu du premier onglet")
#     st.dataframe(data.head())

# with tab2:
#     st.write("Contenu du deuxième onglet")
#     st.table(data.head())

# # Visualisation avec Matplotlib
# fig, ax = plt.subplots()
# ax.plot(data['Age'], data['Fare'], 'o')
# ax.set_xlabel('Âge')
# ax.set_ylabel('Prix du billet')
# st.pyplot(fig)

# # Visualisation avec Seaborn
# fig, ax = plt.subplots()
# sns.histplot(data['Age'], kde=True, ax=ax)
# st.pyplot(fig)

# # Visualisation avec Plotly (Nuage de points interactif)
# fig_plotly = px.scatter(data, x='Age', y='Fare', title="Âge vs Prix du billet")
# st.plotly_chart(fig_plotly)

# # Filtres et interactions
# st.header("Filtres et Interactions")

# # Filtrer par genre (male/female)
# genre = st.selectbox("Sélectionnez le genre à afficher", data['Sex'].unique())
# data_filtre = data[data['Sex'] == genre]
# st.write(f"Affichage des données pour le genre : {genre}")
# st.write(data_filtre)

# # Filtrer par classe (1ère, 2ème, 3ème classe)
# classe = st.selectbox("Sélectionnez la classe à afficher", data['Pclass'].unique())
# data_filtre_classe = data[data['Pclass'] == classe]
# st.write(f"Affichage des données pour la classe {classe}")
# st.write(data_filtre_classe)

# # Filtrer les colonnes à afficher
# colonnes_a_afficher = st.multiselect(
#     "Sélectionnez les colonnes à afficher", 
#     options=data.columns, 
#     default=data.columns[:3]  # Sélectionne les 3 premières colonnes par défaut
# )
# st.write(f"Affichage des colonnes sélectionnées : {colonnes_a_afficher}")
# st.dataframe(data[colonnes_a_afficher])

# # Afficher des informations détaillées sur un point sélectionné dans le graphique (via Plotly)
# fig_plotly = px.scatter(
#     data, 
#     x='Age', 
#     y='Fare', 
#     hover_data=['Name', 'Sex', 'Pclass'],  # Ajoute des informations supplémentaires au survol
#     title="Âge vs Prix du billet avec détails de classe"
# )
# st.plotly_chart(fig_plotly)

# # Mise en cache des données avec st.cache_data
# @st.cache_data
# def charger_donnees(fichier):
#     return pd.read_csv(fichier)

# # Charger les données en utilisant la fonction mise en cache
# data = charger_donnees("test.csv")

# # Initialiser une valeur dans session_state si elle n'existe pas déjà
# if 'compteur' not in st.session_state:
#     st.session_state.compteur = 0

# # Créer des boutons pour augmenter ou diminuer le compteur
# increment = st.button("Incrémenter")
# decrement = st.button("Décrémenter")

# # Mettre à jour la valeur du compteur en fonction des boutons
# if increment:
#     st.session_state.compteur += 1
# if decrement:
#     st.session_state.compteur -= 1

# # Afficher la valeur actuelle du compteur
# st.write(f"Valeur du compteur : {st.session_state.compteur}")

# # Fonction de callback qui s'exécute lorsque le slider est modifié
# def mettre_a_jour():
#     st.session_state['resultat'] = st.session_state['slider_value']

# # Initialiser session_state pour stocker le résultat
# if 'resultat' not in st.session_state:
#     st.session_state['resultat'] = 0

# # Créer un slider avec un callback associé
# st.slider(
#     "Choisissez une valeur", 
#     min_value=1, 
#     max_value=100, 
#     key='slider_value', 
#     on_change=mettre_a_jour  # Appelle la fonction lorsque le slider change
# )

# # Afficher le résultat mis à jour
# st.write(f"Résultat mis à jour : {st.session_state['resultat']}")

# # Permettre aux utilisateurs de télécharger un fichier CSV
# st.header("Téléchargement et gestion des fichiers")
# fichier_telecharge = st.file_uploader("Téléchargez un fichier CSV", type=["csv"])

# if fichier_telecharge is not None:
#     # Lire le fichier CSV téléchargé
#     data_telecharge = pd.read_csv(fichier_telecharge)
#     st.write("Aperçu du fichier téléchargé :")
#     st.write(data_telecharge.head())

# # Télécharger les données sous forme de CSV intitulé 'gender_submission.csv'
# st.download_button(
#     label="Télécharger le fichier CSV",
#     data=data.to_csv(index=False),  # 'data' est le DataFrame utilisé dans ton application
#     file_name='gender_submission.csv',
#     mime='text/csv'
# )

# # Configurer le logging
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# # Ajouter des messages de log dans ton application
# logging.info("Application démarrée")

# # Exemple : Journaliser un message lors du chargement des données
# try:
#     data = pd.read_csv("test.csv")
#     logging.info("Fichier CSV chargé avec succès")
# except FileNotFoundError:
#     logging.error("Le fichier CSV est introuvable")

# # Permettre aux utilisateurs de télécharger un fichier CSV avec une clé unique
# fichier_telecharge = st.file_uploader("Téléchargez un fichier CSV", type=["csv"], key="file_uploader_1")

# if fichier_telecharge is not None:
#     logging.info("Fichier CSV téléchargé par l'utilisateur")
#     data_telecharge = pd.read_csv(fichier_telecharge)
#     st.write("Aperçu du fichier téléchargé :")
#     st.write(data_telecharge.head())

"""
Version améliorée à partir de la Q16
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import logging

# Configurer le logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Application démarrée")

# Mise en cache des données avec st.cache_data
@st.cache_data
def charger_donnees(fichier):
    return pd.read_csv(fichier)

# Charger les données en utilisant la fonction mise en cache
data = charger_donnees("test.csv")
logging.info("Fichier CSV chargé avec succès")

# Titre et en-têtes
st.title("Hello, Streamlit !")
st.header("Dataset du Titanic")
st.subheader("Découverte de streamlit avec ce dataset")
st.write("Utilisation de streamlit avec des données en rapport avec le Titanic")
st.markdown("**Ceci** est réalisé dans le cadre de ma formation chez [Simplon](https://simplon.co)")

# Afficher les premières lignes des données
st.header("Affichage des données du Titanic")
st.subheader("Aperçu des premières lignes")
st.write(data.head())

# Affichage interactif et statique des données
st.subheader("Affichage interactif du DataFrame complet")
st.dataframe(data)

st.subheader("Affichage statique du DataFrame")
st.table(data)

# Widgets Interactifs
st.header("Widgets interactifs")
if st.button("Cliquez ici"):
    st.write("Le bouton a été cliqué!")

if st.checkbox("Afficher les données complètes"):
    st.write(data)

nom_utilisateur = st.text_input("Entrez votre nom")
st.write(f"Bonjour, {nom_utilisateur}.")

# Sélection de colonne et lignes
colonne = st.selectbox("Choisissez une colonne à afficher", data.columns)
st.write(f"Vous avez sélectionné la colonne : {colonne}")
st.write(data[colonne].head())

nb_lignes = st.slider("Choisissez le nombre de lignes à afficher", 1, len(data), 5)
st.write(data.head(nb_lignes))

# Visualisations
st.header("Visualisations")
fig, ax = plt.subplots()
ax.plot(data['Age'], data['Fare'], 'o')
ax.set_xlabel('Âge')
ax.set_ylabel('Prix du billet')
st.pyplot(fig)

fig, ax = plt.subplots()
sns.histplot(data['Age'], kde=True, ax=ax)
st.pyplot(fig)

fig_plotly = px.scatter(data, x='Age', y='Fare', title="Âge vs Prix du billet")
st.plotly_chart(fig_plotly)

# Filtres et interactions
st.header("Filtres et Interactions")
genre = st.selectbox("Sélectionnez le genre à afficher", data['Sex'].unique())
data_filtre = data[data['Sex'] == genre]
st.write(f"Affichage des données pour le genre : {genre}")
st.write(data_filtre)

classe = st.selectbox("Sélectionnez la classe à afficher", data['Pclass'].unique())
data_filtre_classe = data[data['Pclass'] == classe]
st.write(f"Affichage des données pour la classe {classe}")
st.write(data_filtre_classe)

# Colonnes à afficher
colonnes_a_afficher = st.multiselect("Sélectionnez les colonnes à afficher", options=data.columns, default=data.columns[:3])
st.dataframe(data[colonnes_a_afficher])

# Session State et Callbacks
if 'compteur' not in st.session_state:
    st.session_state.compteur = 0

increment = st.button("Incrémenter")
decrement = st.button("Décrémenter")
if increment:
    st.session_state.compteur += 1
if decrement:
    st.session_state.compteur -= 1
st.write(f"Valeur du compteur : {st.session_state.compteur}")

def mettre_a_jour():
    st.session_state['resultat'] = st.session_state['slider_value']

if 'resultat' not in st.session_state:
    st.session_state['resultat'] = 0

st.slider("Choisissez une valeur", min_value=1, max_value=100, key='slider_value', on_change=mettre_a_jour)
st.write(f"Résultat mis à jour : {st.session_state['resultat']}")

# Téléchargement de fichiers
st.header("Téléchargement et gestion des fichiers")
st.download_button(label="Télécharger le fichier CSV", data=data.to_csv(index=False), file_name='gender_submission.csv', mime='text/csv')
