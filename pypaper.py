from ctypes import windll
from os.path import abspath
from os import remove
from urllib.request import urlretrieve
from time import time
from threading import Timer
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


import sqlite3
import random

default_tables = ('Dark_and_Moody', 'Background_Textures', 'Undisturbed_Patterns',
                  'Blurred_in_Motion', 'Winter', 'Amoled', 'Into_the_Wild', 'Micro_Worlds',
                  'Abstract', 'Landscapes', 'Autumn', 'Milkyway', 'Yosemite')

# where to put the image we are downloading
output_filepath = 'output.jpg'
database_filepath = 'database.db'
database_args = detect_types = sqlite3.PARSE_DECLTYPES
last_used = default_tables
frequency = 900
timer = None


def random_wallpaper(tables):
    """
    Gets a new wallpaper and sets it as your background, depending on which database tables you want to search
    """

    global last_used
    last_used = tables
    # print('Updated last used to {}'.format(last_used))

    db = sqlite3.connect(database_filepath, database_args)
    cursor = db.cursor()
    download_url = ''

    result_table = ''

    # pick a random table to use
    if not isinstance(tables, tuple):
        result_table = tables
    else:
        num_tables = tables.__len__() - 1
        result_table = tables[random.randint(0, num_tables)]

    # print('Result table is {}'.format(result_table))

    statement = '''SELECT COUNT(*) FROM {}'''.format(result_table)
    # print(statement)
    cursor.execute(statement)

    num_rows = cursor.fetchone()[0]
    # print('Num_rows is: {}'.format(num_rows))

    id = random.randint(1, num_rows)

    statement = '''SELECT url FROM {} WHERE "id"={}'''.format(result_table, id)
    # print(statement)
    cursor.execute(statement)
    download_url = cursor.fetchone()[0]

    # print(download_url)

    try:
        urlretrieve(download_url, output_filepath)
    except OSError:
        pass
    windll.user32.SystemParametersInfoW(20, 0, abspath(output_filepath),
                                        0)  # sets the wallpaper to the path specified in param 3


def default_paper():
    # print('calling default paper, last used was: {}'.format(last_used))
    random_wallpaper(last_used)


def real_random_paper():
    random_wallpaper(default_tables)


def dark_moody_paper():
    random_wallpaper('Dark_and_Moody')


def background_textures():
    random_wallpaper('Background_Textures')


def undisturbed_paper():
    random_wallpaper('Undisturbed_Patterns')


def blurred_motion_paper():
    random_wallpaper('Blurred_in_Motion')


def winter():
    random_wallpaper('Winter')


def amoled():
    random_wallpaper('Amoled')


def into_the_wild():
    random_wallpaper('Into_the_Wild')


def micro_worlds():
    random_wallpaper('Micro_Worlds')


def abstract():
    random_wallpaper('Abstract')


def landscapes():
    random_wallpaper('Landscapes')


def autumn():
    random_wallpaper('Autumn')


def milkyway():
    random_wallpaper('Milkyway')


def yosemite():
    random_wallpaper('Yosemite')


def close_app():
    try:
        remove(abspath(output_filepath))
    except:
        pass
    timer.cancel()
    QCoreApplication.exit()


class PerpetualTimer:
    """
    A class I got from stack overflow.
    Starts a timer and at the given frequency calls the given function
    frequency is in seconds

    Example:
        from threading import Timer, Thread, Event
        def print_thing():
            print('thing')
        timer = PerpetualTimer(600, print_thing)
        timer.start
    """

    def __init__(self, frequency_seconds, function):
        self.t = frequency_seconds
        self.hFunction = function
        self.thread = Timer(self.t, self.handle_function)

    def handle_function(self):
        self.hFunction()
        self.thread = Timer(self.t, self.handle_function)
        self.thread.start()

    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()


def main():
    """
    Creates the system tray icon and sets up the menu actions for it
    """
    app = QApplication([])
    app.setQuitOnLastWindowClosed(False)

    # Create the icon
    icon = QIcon("icon.jpg")

    # Create the tray
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)

    # Create the menu
    menu = QMenu()

    # the actions we want in our system tray icon's menu
    new_paper = QAction("New Wallpaper")
    random = QAction("All collections")
    close = QAction('Exit')

    new_paper.triggered.connect(default_paper)
    random.triggered.connect(real_random_paper)
    close.triggered.connect(close_app)

    # add the actions to the menu
    menu.addAction(new_paper)
    menu.addAction(random)

    dark_moody = QAction('Dark and Moody')
    background_texture = QAction("Background Textures")
    undisturbed = QAction('Undisturbed Patterns')
    blurred_motion = QAction('Blurred/In Motion')
    wintr = QAction('Winter')
    amled = QAction('Amoled')
    wild = QAction('Into the Wild')
    m_worlds = QAction('Micro Worlds')
    abstrct = QAction('Abstract')
    landscape = QAction('Landscapes')
    autn = QAction('Autumn')
    milk = QAction('Milkyway')
    yosmite = QAction('Yosemite')

    dark_moody.triggered.connect(dark_moody_paper)
    background_texture.triggered.connect(background_textures)
    undisturbed.triggered.connect(undisturbed_paper)
    blurred_motion.triggered.connect(blurred_motion_paper)
    wintr.triggered.connect(winter)
    amled.triggered.connect(amoled)
    wild.triggered.connect(into_the_wild)
    m_worlds.triggered.connect(micro_worlds)
    abstrct.triggered.connect(abstract)
    landscape.triggered.connect(landscapes)
    autn.triggered.connect(autumn)
    milk.triggered.connect(milkyway)
    yosmite.triggered.connect(yosemite)

    menu.addAction(dark_moody)
    menu.addAction(background_texture)
    menu.addAction(undisturbed)
    menu.addAction(blurred_motion)
    menu.addAction(wintr)
    menu.addAction(amled)
    menu.addAction(wild)
    menu.addAction(m_worlds)
    menu.addAction(abstrct)
    menu.addAction(landscape)
    menu.addAction(autn)
    menu.addAction(milk)
    menu.addAction(yosmite)

    menu.addAction(close)

    # Add the menu to the tray
    tray.setContextMenu(menu)

    found = False

    with open('frequency.txt', 'r') as file:
        global frequency
        data = file.read()
        frequency = int(data)
        found = True

    if not found:
        with open('frequency.txt', 'w+') as file:
            file.write(str(frequency))

    global timer
    timer = PerpetualTimer(frequency, default_paper)
    timer.start()
    app.exec_()


if __name__ == '__main__':
    random.seed(time())
    main()

# to export with pyinstaller, add the pipenv path bin to search:
# 'python -OO -m PyInstaller pypaper.py --nowindowed --noconsole -F -p .venv/Lib/site-packages'
