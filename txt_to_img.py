import datetime
from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display
import os
import sys


def path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def nowdate():
    date = datetime.datetime.now()
    date = '{}-{}-{}'.format(date.strftime('%d'), date.strftime('%m'), date.strftime('%Y'))
    return date


def imgtext(period='m', txt='', coordinates=(0, 0), language='', fontsize=30, color='black'):
    match language:
        case 'ar':
            fontpath = path('fonts/HONORSansArabicUI-H.ttf')
            reshaped_txt = arabic_reshaper.reshape(txt)
            txt = get_display(reshaped_txt)
            align = 'right'
        case 'en':
            fontpath = path('fonts/LeagueSpartan-Bold.otf')
            align = 'left'
        case _ :
            fontpath = path('fonts/LeagueSpartan-Bold.otf')
            align = 'center'

    match period:
        case 'm':
            period = '1Morning Period'
        case 'e':
            period = '2Evening Period'

    img = Image.open(path(f'{nowdate()} {period} Daily Report.png'))
    font = ImageFont.truetype(fontpath, fontsize)
    canvas = ImageDraw.Draw(img)
    canvas.text(coordinates, txt, color, font=font, align=align)
    img.save(path(f'{nowdate()} {period} Daily Report.png'))