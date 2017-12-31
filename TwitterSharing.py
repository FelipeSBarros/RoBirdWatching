# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 19:17:38 2017

@author: felipe
"""

import twitter

#import accessTolkens
#os.system('python /home/felipe/Raspberry/Robirdwatching/accessTolkens.py')

def postTwipy(comicAlt, comicDate, path):
    api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_tolken,
                  access_token_secret=access_tolken_secret)
    
    api.PostUpdate(status='Todays\' Doodle ', media = path)
    
def noDoodle():
    api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_tolken,
                  access_token_secret=access_tolken_secret)
    
    api.PostUpdate('Unfortunatly, no new Doodle today')