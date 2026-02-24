import qrcode 
from qrcode.constants import ERROR_CORRECT_L

var= qrcode.QRCode(
    version=3,
    error_correction=ERROR_CORRECT_L,
    box_size=3,
    border=5
)

var.add_data('www.gouaboCodingCity.con')
var.make(fit=True)

varColor =var.make_image(fill_color="green",back_color="white")
varColor.save('vert.png')
