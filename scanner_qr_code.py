import cv2
from pyzbar.pyzbar import decode

def lire_qrcode():
    cap = cv2.VideoCapture(0)  # 0 = caméra par défaut

    print("📷 Ouverture de la caméra... Appuie sur 'q' pour quitter.")

    while True:
        success, frame = cap.read()
        if not success:
            break

        # Lecture des QR codes dans le frame
        for qr in decode(frame):
            data = qr.data.decode('utf-8')
            print(f"✅ QR Code détecté : {data}")
            # Encadrer le QR Code
            (x, y, w, h) = qr.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        cv2.imshow("📸 Scanner QR Code", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("👋 Caméra fermée.")

if __name__ == "__main__":
    lire_qrcode()
