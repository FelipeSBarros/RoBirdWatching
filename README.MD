# Robotwatching Project #100DaysOfCode
This is one of the diferents repositories that I will be using during my commitment with #100DaysOfCode.  

**About this project:**  
The ideia is to build a trap cam using Raspberry PI, with usb cam and movment sensor, so every time a bird come to my window to eat the fruits, It takes a picture and share with me the picture took by telegram and/or twitter. A audacious goal I set with this project is build a machine learning to identify the species in the picture taken. Not sure how futher I will go, so I will try to work modularly:  
**Module 1:** Build the workflow and function to get some data and sharing it on a twitter bor; :white_check_mark: You can find this module [here](https://github.com/FelipeSBarros/1stRoBirdWatchingModule)  
**Module 2:** Build on #RaspBerry a trigger with movement sensor so everytime a bird come by the window a picture of him is taken;  
**Module 3:** Build a machine learning (possible with #TensorFlow and/or #OpenCV for computer vision) to identfy the bird species from the picture took on Module2;  
**Module 4:** Join both previous module in one workflow  

But the idea is the enjoy the process and learn also about SQLite3.

Again: the idea is to build this in a modular way, divided in diferent functionalities, so I can learn trhu the process.

## Setting up the programming environment:

### First step: update, upgrade and install sotwares
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

## Installing the modules needed
```
pip install bs4
pip install requests
pip install python-twitter
```
