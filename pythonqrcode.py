import qrcode
from qrcode.constants import ERROR_CORRECT_L

var = qrcode.QRCode(
    version =5,
    error_correction =ERROR_CORRECT_L,
    box_size = 5,
    border = 10
)

var.add_data('le programme python qui permet de générer un Qr code')
var.make(fit=True)

varColor = var.make_image(fill_color="black",back="white")
varColor.save('C:/fireforx/Bureau doc/QR CODE/programmeQR.png')