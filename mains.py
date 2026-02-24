import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Création d'un graphique pour représenter l'aménagement de l'espace de La Ferme Houle
fig, ax = plt.subplots(figsize=(10, 8))

# Création de zones sur l'espace de 2 hectares
# Zone de culture
ax.add_patch(patches.Rectangle((0, 0), 1, 1, linewidth=1, edgecolor='green', facecolor='lightgreen', label="Zone de culture"))

# Zone d'élevage
ax.add_patch(patches.Rectangle((1, 0), 0.5, 0.5, linewidth=1, edgecolor='brown', facecolor='lightyellow', label="Zone d'élevage"))

# Zone de transformation
ax.add_patch(patches.Rectangle((0.5, 1), 0.2, 0.2, linewidth=1, edgecolor='orange', facecolor='lightcoral', label="Zone de transformation"))

# Zones de stockage et de gestion
ax.add_patch(patches.Rectangle((0.7, 0.8), 0.1, 0.1, linewidth=1, edgecolor='grey', facecolor='lightgray', label="Stockage et gestion"))

# Restaurant
ax.add_patch(patches.Rectangle((1.5, 0.5), 0.3, 0.3, linewidth=1, edgecolor='blue', facecolor='lightskyblue', label="Restaurant"))

# Espaces verts et éducatifs
ax.add_patch(patches.Rectangle((0.8, 1.2), 0.2, 0.3, linewidth=1, edgecolor='forestgreen', facecolor='mediumseagreen', label="Espace éducatif"))

# Chemins d'accès
ax.plot([0.5, 0.7], [0, 0], color='grey', lw=2)  # chemin principal
ax.plot([0.7, 1], [0, 0], color='grey', lw=2)    # chemin d'accès

# Légende et titres
ax.set_title("Plan de l'exploitation agropastorale La Ferme Houle", fontsize=16)
ax.legend(loc='upper right', fontsize=10)

# Paramétrage des axes et affichage
ax.set_xlim(0, 2)
ax.set_ylim(0, 2)
ax.set_aspect('equal', 'box')
ax.axis('off')  # On enlève les axes pour une vue plus claire

plt.show()