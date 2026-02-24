cap = cv2.VideoCapture(0)

# Capture une image
ret, frame = cap.read()

# Enregistre l'image
cv2.imwrite("photo.jpg", frame)

# Ferme la webcam
cap.release()