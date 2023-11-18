import bz2
import os.path
import urllib.request
import shutil
import filer
"""
Downloads the latest sqlite-latest.sqlite.bz2 file from https://www.fuzzwork.co.uk/dump/
"""


def getLatestBz2():
    """
    Downloads the latest sqlite-latest.sqlite.bz2 file from https://www.fuzzwork.co.uk/dump/
    :return: 1 if the file was downloaded successfully, 0 otherwise
    """
    # Downloading the latest sqlite-latest.sqlite.bz2 file
    url = 'https://www.fuzzwork.co.uk/dump/sqlite-latest.sqlite.bz2'
    with urllib.request.urlopen(url) as response, open('sqlite-latest.sqlite.bz2', 'wb') as out_file:
        shutil.copyfileobj(response, out_file)

    # Extracting the sqlite-latest.sqlite.bz2 file
    with bz2.open('sqlite-latest.sqlite.bz2', 'rb') as f:
        file_content = f.read()
        with open('sqlite-latest.sqlite', 'wb') as out_file:
            out_file.write(file_content)

    if os.path.isfile('sqlite-latest.sqlite'):
        return 1
    else:
        return 0


def getCurrentDBVersion():
    """
    Scraps the current version of the database from https://www.fuzzwork.co.uk/dump/
    :return: the current version of the database
    """
    url = 'https://www.fuzzwork.co.uk/dump/'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        html = html.decode('utf-8')
        html = html.split('\n')
        for line in html:
            if 'sqlite-latest.sqlite.bz2' in line:
                return line.split(' ')[-1].split('.')[0]


def checkNewDB():
    """
    Checks if there is a new database available, and if there is, downloads it
    :return: None
    """
    installed_version = filer.getVersionJson()['installed_db_version']
    current_version = getCurrentDBVersion()
    if installed_version != current_version:
        getLatestBz2()
        filer.writeVersionJson({'installed_db_version': current_version})
