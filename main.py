from txt_to_img import imgtext, nowdate
import shutil
import gui
import os
import sys

"""
date (510, 150, 50)
imgtext(date, (510, 150), 'en', 50, 'white')

(110, 440) (760, 440)
(105, 555) (760, 555)
(150, 665) (760, 665)
(90, 1035) (710, 780)
(150, 885) (710, 885)
(90, 1035)

nums max 3, 4, 5
imgtext(period, '٢', (760, 440), 'ar', 80, 'black')

ar txt max 17
imgtext('', (660, 1030), 'ar', 26, 'black')

manager
imgtext(period, manager, (400, 1142), 'en', 45, (131, 35, 35))

leaders max 54
imgtext(period, 'Mazen Magdy - Amal Kamel - Farah - Hassan - Zarkaria', (200, 1215), 'en', 30, 'black')

"""


def path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


valuesdict = {
    'nums': {
        (760, 440): '',
        (760, 555): '',
        (760, 665): '',
        (710, 780): '',
        (710, 890): '',
        (110, 440): '',
        (105, 560): '',
        (150, 665): '',
        (150, 885): '',
    },
    'words': {
        (110, 810): '',
        (110, 1035): ''
    }

}


def shiftmanager(who):
    match who:
        case 1:
            manager = 'Mahmoud Awad'
        case 2:
            manager = 'Mohamed Abdeljelel'
        case None:
            manager = ''
    return manager


def leaders(namelist):
    leaders = ''
    for name in namelist:
        if name:
            if leaders:
                leaders += f' - {name}'
            else:
                leaders = name
    return leaders


def drawer(period, shift, leaders, manager, valuesdict):
    imgtext(period, nowdate(), (510, 150), 'en', 50, 'white')
    imgtext(period, shift, (550, 200), 'ar', 40, 'white')
    imgtext(period, shiftmanager(manager), (400, 1142), 'en', 45, (151, 35, 35))
    imgtext(period, leaders, (200, 1215), 'en', 30, 'black')
    for coordinate in valuesdict.get('nums'):
        imgtext(period, valuesdict.get('nums').get(coordinate), coordinate, 'ar', 80, 'black')
    for coordinate in valuesdict.get('words'):
        imgtext(period, valuesdict.get('words').get(coordinate), coordinate, 'ar', 30, 'black')


def imgexport(period, leaders, manager, valuesdict):
    match period:
        case 'm':
            period = '1Morning Period'
            shift = 'شيفت صباحي'
        case 'e':
            period = '2Evening Period'
            shift = 'شيفت مسائي'

    shutil.copy(str(path('data/daily_report.png')), str(path(f'{nowdate()} {period} Daily Report.png')))
    drawer(period, shift, leaders, manager, valuesdict)


# script
def export():
    valuesdict['nums'][(760, 440)] = gui.entry1.get()
    valuesdict['nums'][(760, 555)] = gui.entry2.get()
    valuesdict['nums'][(760, 665)] = gui.entry3.get()
    valuesdict['nums'][(710, 780)] = gui.entry4.get()
    valuesdict['nums'][(710, 890)] = gui.entry5.get()
    valuesdict['nums'][(110, 440)] = gui.entry6.get()
    valuesdict['nums'][(105, 560)] = gui.entry7.get()
    valuesdict['nums'][(150, 665)] = gui.entry8.get()
    valuesdict['nums'][(150, 885)] = gui.entry9.get()

    valuesdict['words'][(110, 810)] = gui.entry10.get()
    valuesdict['words'][(110, 1035)] = gui.entry11.get()

    match gui.period.get():
        case 1:
            theperiod = 'm'
        case 2:
            theperiod = 'e'

    def leaders(*args):
        leaders = ''
        for arg in args:
            if arg:
                if leaders:
                    leaders += f' - {arg}'
                else:
                    leaders = arg
        return leaders

    imgexport(theperiod, leaders(gui.entry13.get(), gui.entry14.get(), gui.entry15.get(), gui.entry16.get()),
              gui.manager.get(), valuesdict)

