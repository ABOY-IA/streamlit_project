import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import io

# Titre de l'application
st.title("Outil d'analyse de données interactif")

# 1. Chargement des données
st.header("Chargement de données")
uploaded_file = st.file_uploader("Téléchargez un fichier CSV", type=["csv"])

if uploaded_file is not None:
    # Lire le fichier CSV
    data = pd.read_csv(uploaded_file)
    st.success("Fichier chargé avec succès !")

    # 2. Exploration des données
    st.header("Exploration des données")
    
    # Afficher les premières lignes
    st.subheader("Aperçu des premières lignes")
    st.write(data.head())
    
    # Afficher les statistiques descriptives
    st.subheader("Statistiques descriptives")
    st.write(data.describe())
    
    # Afficher le résumé des types de données et des valeurs manquantes
    st.subheader("Résumé des données")
    buffer = io.StringIO()
    data.info(buf=buffer)
    st.text(buffer.getvalue())

    # Sélectionner les colonnes à afficher
    st.subheader("Sélection des colonnes")
    colonnes_selectionnees = st.multiselect("Sélectionnez les colonnes à afficher", options=data.columns)
    
    if colonnes_selectionnees:
        st.write(data[colonnes_selectionnees].head())
    
    # 3. Visualisation interactive
    st.header("Visualisation interactive")
    
    # Sélectionner les colonnes pour le graphique
    x_col = st.selectbox("Sélectionnez la colonne pour l'axe X", options=data.columns)
    y_col = st.selectbox("Sélectionnez la colonne pour l'axe Y", options=data.columns)
    
    # Choix du type de graphique
    type_graphique = st.selectbox("Choisissez le type de graphique", options=["Nuage de points", "Histogramme", "Courbe"])

    fig, ax = plt.subplots()

    if type_graphique == "Nuage de points":
        st.subheader(f"Nuage de points : {x_col} vs {y_col}")
        sns.scatterplot(data=data, x=x_col, y=y_col, ax=ax)
    
    elif type_graphique == "Histogramme":
        st.subheader(f"Histogramme de {x_col}")
        nb_bins = st.slider("Choisissez le nombre de bacs", min_value=5, max_value=50, value=10)
        ax.hist(data[x_col], bins=nb_bins, color="skyblue", edgecolor="black")
    
    elif type_graphique == "Courbe":
        st.subheader(f"Courbe : {x_col} vs {y_col}")
        ax.plot(data[x_col], data[y_col], color="blue", linewidth=2)

    st.pyplot(fig)

    # Ajouter un bouton pour télécharger le graphique
    img_buffer = io.BytesIO()
    fig.savefig(img_buffer, format="png")
    img_buffer.seek(0)
    st.download_button(label="Télécharger le graphique", data=img_buffer, file_name="graphique.png", mime="image/png")

    # 4. Filtrage des données
    st.header("Filtrage des données")
    
    # Sélectionner une colonne et une valeur pour filtrer
    col_filtre = st.selectbox("Sélectionnez la colonne pour filtrer", options=data.columns)
    valeurs_filtre = st.selectbox(f"Valeur dans la colonne '{col_filtre}'", options=data[col_filtre].unique())
    
    # Afficher les données filtrées
    data_filtre = data[data[col_filtre] == valeurs_filtre]
    st.write(data_filtre)

    # Ajouter un bouton pour télécharger les données filtrées en CSV
    csv_buffer = io.BytesIO()
    csv_buffer.write(data_filtre.to_csv(index=False).encode('utf-8'))
    csv_buffer.seek(0)  # Repositionner au début du fichier

    st.download_button(
        label="Télécharger les données filtrées en CSV", 
        data=csv_buffer, 
        file_name="donnees_filtrees.csv", 
        mime="text/csv"
    )

else:
    st.warning("Veuillez télécharger un fichier CSV pour commencer l'analyse.")
