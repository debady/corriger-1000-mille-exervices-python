import cv2
import numpy as np
from pyzbar.pyzbar import decode

def read_qr_code(image_path):
    # Charger l'image
    image = cv2.imread(image_path)
    
    # Décoder le QR code
    qr_codes = decode(image)
    
    if qr_codes:
        for qr in qr_codes:
            data = qr.data.decode('utf-8')  # Extraire et décoder les données
            print(f"QR Code détecté : {data}")
        return data
    else:
        print("Aucun QR Code détecté.")
        return None

# Exemple d'utilisation
image_path = "C:/Users/NGUESSAN.DESKTOP-38E6PIP/Desktop/SohapiGroup/hostolink/assets/images/qr-code-test.png"  # Remplace par le chemin de ton image
read_qr_code(image_path)
