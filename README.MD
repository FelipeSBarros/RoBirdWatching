# Robotwatching Project #100DaysOfCode
This is one of the diferents repositories that I will be using during my commitment with #100DaysOfCode.

**About this project**:
The ideia is to build a trap cam using Raspberry PI, with usb cam and movment sensor, so every time a bird come to my window to eat the fruits, It takes a picture and share with me the picture took by telegram and/or twitter. But the idea is the enjoy the process and learn also about SQLite3.

So the idea is to build this in a modular way, divided in diferent functionalities, so I can learn
trhu the process. And dispite having the Raspberry PI, I don't have the camera neighter the sensor, so I decided to start by playing with python, creating a process of acquiring some data from the internet routinely (in this case I will wabscrap to cheack and download every google Doodles), saving it on SQLite and share this data in telegram or twitter. 

## First step: update, upgrade and install sotwares
```
# Updating and upgrading the environment
sudo apt-get update && sudo apt-get -y upgrade && sudo apt-get autoremove && sudo apt-get autoclean && sudo apt-get clean
# Installing SQLite3
sudo apt-get install sqlite3

# To check python version
python3 -V
```
Will return:
```
Python 3.5.2
```
Instaling packages manager pip for python 3:
```
sudo apt-get install -y python3-pip
# And a few more packages sugested by: https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04
sudo apt-get install build-essential libssl-dev libffi-dev python-dev
```
### Creating virtual environment
```
sudo apt-get install -y python3-venv
# Creating a folder for the virtualenv:
mkdir Raspberry && cd Raspberry
python3 -m venv Robirdwatching

# Activating the virtual env;
source Robirdwatching/bin/activate
```
**Note: Within the virtual environment, you can use the command python instead of python3, and pip instead of pip3 if you would prefer. If you use Python 3 on your machine outside of an environment, you will need to use the python3 and pip3 commands exclusively.**

**To leave the environment, simply type the command deactivate and you will return to your original directory.**

### Creating SQLite3 data base
```
sqlite3 mydb.db
# Creating the tables

sqlite> CREATE TABLE Images(Id INTEGER PRIMARY KEY, Data BLOB); # to save the images
sqlite> CREATE TABLE Metadata(Id INTEGER PRIMARY KEY, Date TEXT, Legend TEXT, Path TEXT); # to save information about the images
```
Checking sqlite3 version with python

```
$ python
import sqlite3
sqlite3.version
sqlite3.sqlite_version
# Will return, respectively:
'2.6.0'
'3.11.0'
```
## Installing the modules needed
```
pip install bs4
pip install requests
pip install python-twitter
```

Back to the idea:
Idea: 
1. donwalod google doodle image with python beatiful soup; :white_check_mark:
2. Execute this function every day; :white_check_mark:
3. Save result to Data base; :white_check_mark:
4. send result by telegram and twitter; :white_check_mark:
source https://automatetheboringstuff.com/chapter11/
