# PyPaper

One of the first things I ever made, at least outside of programming class. Definitely could use a lot of love, but it works I guess.

A wallpaper app built with python and scraped data from unsplash. Only works on Windows currently, but could be modified in the future for unix systems (just need to change the windows specific wallpaper setting  code). Scraped data comes from (Paper scraper)[https://github.com/Pachwenko/Paper-Scraper] and is stored in database.db using sqlite3. There are 13 different collections to choose from including all combined.

PyQt5 Is used for the system tray GUI, but not for changing the frequency.

## How to run

If you want to use this like a normal user you can download from the releases page and run the main.exe file. It must be in the folder with its required files. I'm not sure how to actually install this like a genuine windows app, maybe it can just be plopped in some folder? - TODO

Otherwise, you can set up a python environment and run it that way:

[Install python](https://www.python.org/), as of writing I am using 3.9.
First, [install poetry to manage python dependencies](https://python-poetry.org/).

```powershell
poetry install
poetry shell
python main.py
```

Open your system tray to see the application.


## How to use

When running an icon should appear in your system tray. Click on the icon to see all options, once a selection has been made it will be remembered untill the program closes.
Note: Certain files must exist in the folder you run the application from.

### Changing frequency

Edit the "frequency.txt" file and put ONLY your desired number of seconds between wallpaper changes.