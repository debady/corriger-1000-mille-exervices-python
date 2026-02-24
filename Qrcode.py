import qrcode
from qrcode.constants import ERROR_CORRECT_L

var =qrcode.QRCode(
    version = 5,
    error_correction = ERROR_CORRECT_L,
    box_size = 5,
    border = 10
)
var.add_data('programme python qui génère un Qr code !')
var.make(fit=True)

varColor = var.make_image(fill_color="black",back="white")
varColor.save('C:/[{chemin complete de l\'endroit ou vous souhaitez enregistrer votre qrcode} /qr.png')
varColor.save('Monqr.png')

#youtube :www.youtube.com/@NK2DCoding-City