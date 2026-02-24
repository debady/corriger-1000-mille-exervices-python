import cv2
from pyzbar.pyzbar import decode

def scan_qr_webcam():
    cap = cv2.VideoCapture(0)  # Ouvrir la webcam
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Décoder les QR codes dans l'image de la webcam
        qr_codes = decode(frame)
        for qr in qr_codes:
            data = qr.data.decode('utf-8')  # Extraire les données
            print(f"QR Code détecté : {data}")
            cap.release()
            cv2.destroyAllWindows()
            return data

        cv2.imshow("Scanner QR Code", frame)
        
        # Quitter avec la touche 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Lancer le scanner
scan_qr_webcam()
