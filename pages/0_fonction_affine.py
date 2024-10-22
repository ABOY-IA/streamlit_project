import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Titre de l'application
st.title("Visualisation interactive d'une fonction affine")

# Sliders interactifs pour contrôler a (pente) et b (ordonnée à l'origine)
a = st.slider("Pente (a)", min_value=-10.0, max_value=10.0, value=1.0, step=0.1)
b = st.slider("Ordonnée à l'origine (b)", min_value=-10.0, max_value=10.0, value=0.0, step=0.1)

# Génération des valeurs de x et calcul des valeurs de y
x = np.linspace(-10, 10, 400)
y = a * x + b

# Création du graphique avec Matplotlib
fig, ax = plt.subplots()
ax.plot(x, y, label=f"y = {a}x + {b}")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.axhline(0, color='black',linewidth=0.5)
ax.axvline(0, color='black',linewidth=0.5)
ax.grid(True)
ax.legend()

# Affichage du graphique dans Streamlit
st.pyplot(fig)

# Affichage de l'équation
st.write(f"L'équation de la droite est : y = {a}x + {b}")
