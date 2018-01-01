#!/usr/bin/python
# downloadGDoodles.py - Downloads every single google's Doodles;

import requests, os, bs4
import sqlite3 as lite
import sys
from compareFunction import DoodleTest
from TwitterSharing import noDoodle, postTwipy

url = 'https://www.google.com/doodles'              # starting url
os.makedirs('Doodles', exist_ok=True)   # store doodles in ./Doodles

# Download the page.
print('Downloading page %s...' % url)
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)

# Find the URL of the comic image.
comicElem = soup.select('#latest img')

if comicElem == []: # if could find the image
    print('Could not find new Doodle.')
else:
    try:
        comicUrl = 'http:' + comicElem[0].get('src')
        res = requests.get(comicUrl)
        res.raise_for_status()
        comicAlt = comicElem[0].get('alt') # getting the alt text of the image
        comicDate = soup.select('#latest-tag')[0].text # getting the date
    except requests.exceptions.MissingSchema:
        # skip this comic
        prevLink = soup.select('a[rel="prev"]')[0]
        url = 'https://www.google.com/doodles' + prevLink.get('href')

testResult = DoodleTest(comicAlt) # testing if the Doodle is new or tehre is one already saved on database
if testResult is None or testResult is False:
    # Save the image to ./xkcd.
    print('Downloading image %s...' % (comicUrl))
    imageFile = open(os.path.join('Doodles', os.path.basename(comicUrl)), 'wb')
    path = str(os.path.join('Doodles', os.path.basename(comicUrl)))
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)

    imageFile.close()

    values = (comicDate,
              #.encode('ascii', 'ignore'), 
              comicAlt,#.encode('ascii', 'ignore'), 
    path)
    
    print('Sharing on twitter!')
    postTwipy(comicAlt, comicDate, path)

    try:
        print('Image saved; Saving data to SQLite')
        con = lite.connect('/home/felipe/Raspberry/Robirdwatching/mydb.db')
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
else:
    noDoodle()