import random
import string

import segno


def create_code(data, color):
    name = ''.join(random.choices(string.ascii_uppercase, k=random.randint(5, 32)))
    filename = f'images/{name}.png'

    qrcode = segno.make_qr(data)
    qrcode.save(filename, scale=15, dark=color)

    return filename
