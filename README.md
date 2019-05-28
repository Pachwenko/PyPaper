# PyPaper
A wallpaper app built with python and scraped data from unsplash. Only works on Windows 10 currently, but may be modified in the future for unix systems. Scraped data comes from (Paper scraper)[https://github.com/Pachwenko/Paper-Scraper] and is stored in database.db using sqlite3. There are 13 different collections to choose from including all combined.

PyQt5 Is used for the system tray GUI, but not for changing the frequency.

## How to run

See (releases page)[https://github.com/Pachwenko/PyPaper/releases]
Preferably download the .exe from releases page and run that.

To run from source you need to install the requirements first.
To do so,
```bash
pip install -r requirements.txt
```

## How to use

After running then an icon should appear in your system tray. Click on the icon to see all options, once a selection has been made it will be remembered untill the program closes.
Note: Make sure the icon.jpg is in the root folder of the program, if not then nothing will appear in the system tray.

### Changing frequency

Edit the "frequency.txt" file and put ONLY your desired number of seconds between wallpaper changes.

## Requirements

 - PyQt5==5.12.2
 - PyQt5-sip==4.19.17
