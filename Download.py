#!/usr/bin/python
# downloadGDoodles.py - Downloads every single google's Doodles;

import requests, os, bs4
import sqlite3 as lite
import sys
from compareFunction import DoodleTest

url = 'https://www.google.com/doodles'              # starting url
os.makedirs('Doodles', exist_ok=True)   # store doodles in ./Doodles

# Download the page.
print('Downloading page %s...' % url)
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)

# Find the URL of the comic image.
comicElem = soup.select('#latest img')

if comicElem == []:
    print('Could not find comic image.')
else:
    try:
        comicUrl = 'http:' + comicElem[0].get('src')
        res = requests.get(comicUrl)
        res.raise_for_status()
        comicAlt = comicElem[0].get('alt')
        comicDate = soup.select('#latest-tag')[0].text
    except requests.exceptions.MissingSchema:
        # skip this comic
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'https://www.google.com/doodles' + prevLink.get('href')

testResult = DoodleTest(comicAlt)
if testResult is None or testResult is False:
    # Save the image to ./xkcd.
    print('Downloading image %s...' % (comicUrl))
    imageFile = open(os.path.join('Doodles', os.path.basename(comicUrl)), 'wb')
    path = str(os.path.join('Doodles', os.path.basename(comicUrl)))
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)

    imageFile.close()

    print('Image saved; Saving data to SQLite')

    values = (comicDate,
              #.encode('ascii', 'ignore'), 
              comicAlt,#.encode('ascii', 'ignore'), 
    path)

    try:
        con = lite.connect('mydb.db')
        cur = con.cursor()
        cur.execute("INSERT INTO Metadata(Date, Legend, Path) VALUES(?,?,?)",values)
        con.commit()
    except lite.Error as e:
        if con:
            con.rollback()
            print("Error %s:" % e.args[0])
            sys.exit(1)
    finally:
        if con:
            con.close() 