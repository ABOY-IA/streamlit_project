# version basique avec ce qui est demandé


# import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt

# # Titre de l'application
# st.title("Visualisation interactive d'une fonction affine")

# # Sliders interactifs pour contrôler a (pente) et b (ordonnée à l'origine)
# a = st.slider("Pente (a)", min_value=-10.0, max_value=10.0, value=1.0, step=0.1)
# b = st.slider("Ordonnée à l'origine (b)", min_value=-10.0, max_value=10.0, value=0.0, step=0.1)

# # Génération des valeurs de x et calcul des valeurs de y
# x = np.linspace(-10, 10, 400)
# y = a * x + b

# # Création du graphique avec Matplotlib
# fig, ax = plt.subplots()
# ax.plot(x, y, label=f"y = {a}x + {b}")
# ax.set_xlabel("x")
# ax.set_ylabel("y")
# ax.axhline(0, color='black',linewidth=0.5)
# ax.axvline(0, color='black',linewidth=0.5)
# ax.grid(True)
# ax.legend()

# # Affichage du graphique dans Streamlit
# st.pyplot(fig)

# # Affichage de l'équation
# st.write(f"L'équation de la droite est : y = {a}x + {b}")


# version améliorée avec choix des couleurs


# import streamlit as st
# import numpy as np
# import matplotlib.pyplot as plt

# # Titre de l'application
# st.title("Visualisation interactive d'une fonction affine")

# # Sliders interactifs pour contrôler a (pente) et b (ordonnée à l'origine)
# a = st.slider("Pente (a)", min_value=-10.0, max_value=10.0, value=1.0, step=0.1)
# b = st.slider("Ordonnée à l'origine (b)", min_value=-10.0, max_value=10.0, value=0.0, step=0.1)

# # Slider pour choisir l'intervalle de x
# x_min = st.slider("Valeur minimale de x", min_value=-20, max_value=0, value=-10)
# x_max = st.slider("Valeur maximale de x", min_value=0, max_value=20, value=10)

# # Génération des valeurs de x et calcul des valeurs de y
# x = np.linspace(x_min, x_max, 400)
# y = a * x + b

# # Option pour personnaliser la couleur de la courbe
# couleur = st.color_picker("Choisissez la couleur de la courbe", "#00f900")

# # Options pour personnaliser les titres et étiquettes
# titre_graphique = st.text_input("Titre du graphique", "Graphique de la fonction affine")
# label_x = st.text_input("Étiquette pour l'axe x", "x")
# label_y = st.text_input("Étiquette pour l'axe y", "y")

# # Création du graphique avec Matplotlib
# fig, ax = plt.subplots()
# ax.plot(x, y, color=couleur, label=f"y = {a}x + {b}")
# ax.set_xlabel(label_x)
# ax.set_ylabel(label_y)
# ax.axhline(0, color='black', linewidth=0.5)
# ax.axvline(0, color='black', linewidth=0.5)
# ax.grid(True)
# ax.legend()
# ax.set_title(titre_graphique)

# # Affichage du graphique dans Streamlit
# st.pyplot(fig)

# # Affichage de l'équation
# st.write(f"L'équation de la droite est : y = {a}x + {b}")


# version encore plus avancée

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Titre de l'application
st.title("Visualisation interactive d'une fonction affine avec MSE et MAE")

# Sliders interactifs pour contrôler a (pente) et b (ordonnée à l'origine)
a = st.slider("Pente (a)", min_value=-10.0, max_value=10.0, value=1.0, step=0.1)
b = st.slider("Ordonnée à l'origine (b)", min_value=-10.0, max_value=10.0, value=0.0, step=0.1)

# Génération des valeurs de x
x = np.linspace(-10, 10, 400)

# Génération de la droite affine
y_affine = a * x + b

# Génération des points aléatoires (bruit gaussien) avec la même longueur que la droite affine
points_aleatoires = y_affine + np.random.randn(len(x))

# Etape 2: Calcul du MSE (Erreur Quadratique Moyenne)
mse = np.mean((y_affine - points_aleatoires) ** 2)

# Bonus: Calcul du MAE (Erreur Absolue Moyenne)
mae = np.mean(np.abs(y_affine - points_aleatoires))

# Stocker les valeurs de a et du MSE dans une liste
historique_a_mse = []

# Afficher le graphique de la fonction affine avec les points aléatoires
fig, ax = plt.subplots()
ax.plot(x, y_affine, label=f"Droite affine : y = {a}x + {b}", color="blue")
ax.scatter(x, points_aleatoires, label="Points aléatoires", color="red", marker="o")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
ax.grid(True)

# Afficher le graphique dans Streamlit
st.pyplot(fig)

# Affichage de l'équation et du MSE
st.write(f"L'équation de la droite est : y = {a}x + {b}")
st.write(f"Erreur Quadratique Moyenne (MSE) : {mse:.4f}")
st.write(f"Erreur Absolue Moyenne (MAE) : {mae:.4f}")

# Etape 3: Afficher le MSE en fonction de "a"
# Calcul du MSE pour différentes valeurs de "a" (avec un "b" constant)
valeurs_a = np.linspace(-10, 10, 100)
mse_a = [np.mean((a_i * x + b - points_aleatoires) ** 2) for a_i in valeurs_a]

# Graphique du MSE en fonction de "a"
fig2, ax2 = plt.subplots()
ax2.plot(valeurs_a, mse_a, label="MSE en fonction de a", color="green")
ax2.set_xlabel("Valeur de a")
ax2.set_ylabel("MSE")
ax2.grid(True)
ax2.legend()

# Afficher le graphique du MSE en fonction de "a"
st.pyplot(fig2)

# Bonus: Réflexion sur l'influence de "b" et trouver la valeur de "a" qui minimise le MSE
index_min_mse = np.argmin(mse_a)
a_optimal = valeurs_a[index_min_mse]
st.write(f"La valeur de 'a' qui minimise le MSE est : {a_optimal:.2f}")

# Bonus: Utiliser MAE au lieu du MSE pour minimiser
mae_a = [np.mean(np.abs(a_i * x + b - points_aleatoires)) for a_i in valeurs_a]
index_min_mae = np.argmin(mae_a)
a_optimal_mae = valeurs_a[index_min_mae]
st.write(f"La valeur de 'a' qui minimise le MAE est : {a_optimal_mae:.2f}")

