import qrcode
from PIL import Image
import os

def generer_qrcode(texte, chemin_image=None, sortie='qrcode.png', taille_logo=100):
    # Générer le QR code de base
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Haute correction d'erreur
        box_size=10,
        border=4,
    )
    qr.add_data(texte)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    # Ajouter une image au centre si fournie
    if chemin_image and os.path.exists(chemin_image):
        logo = Image.open(chemin_image)
        
        # Redimensionner le logo
        logo = logo.resize((taille_logo, taille_logo), Image.LANCZOS)

        # Calcul de la position du logo au centre
        pos = (
            (qr_img.size[0] - logo.size[0]) // 2,
            (qr_img.size[1] - logo.size[1]) // 2
        )

        qr_img.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)

    qr_img.save(sortie)
    print(f"QR Code enregistré sous : {sortie}")

# Exemple d'utilisation
if __name__ == "__main__":
    texte = input("Entrez le texte à encoder dans le QR Code : ")
    image = input("Chemin de l'image à insérer (laisser vide si aucune) : ").strip() or None
    generer_qrcode(texte, image)
