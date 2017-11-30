from twython import Twython
import blinkt
import time
import csv
import string
import sys
import colorsys
import time
from blinkt import set_brightness, set_pixel, show

blinkt.clear()
blinkt.show()

APP_KEY = 'Fyu91pHPzP7PnHrjeJCVO92KA'
APP_SECRET = 'WOSLUjfqmxtCNxCBtorrIHmTmtAjcFgM2qKL6xUPukeHIPm2s5'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

with open('colours.csv', 'Ur') as f:
	reader = csv.reader(f)
	colours = list(reader)

def hex_to_rgb(hex):
	if len(hex) == 3:
		hex = hex[0] + hex[0] + hex[1] + hex[1] + hex[2] + hex[2]
	r = hex[0:1]
	g = hex[2:3]
	b = hex[4:5]
	r = int(r, base=16)
	g = int(g, base=16)
	b = int(b, base=16)
	return r, g, b

def colourCheck(inputstring):
    inputstring_lc = inputstring.lower()
    print(inputstring_lc)
    punctuations = set(string.punctuation)
    inputstring_np = ''.join(char for char in inputstring_lc if char not in punctuations)
    print(inputstring_np)
    
    for i in range(1,len(colours)):
        if colours[i][0] in inputstring_np:
            print(colours[i][1][1:])
            return(colours[i][1][1:])
        	
def rainbowit():
	spacing = 360.0 / 16.0
	hue = 0
	set_brightness(0.1)
	
	for i in range(500):	
		hue = int(time.time() * 100) % 360
		for x in range(8):
			offset = x * spacing
			h = ((hue + offset) % 360) / 360.0
			r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
			set_pixel(x, r, g, b)
		show()
		time.sleep(0.001)

while True:
    search = twitter.search(q='#cheerlights')
    tweets = search['statuses']
    twindex = 0
    haveSetColour = False
    while not haveSetColour:
        print(type(tweets[0]['text']))
        print(type(u' '))
        tweet = u' ' + tweets[twindex]['text'] + u' '
        if 'rainbow' in tweet.lower():
            haveSetColour = True
            rainbowit()
        elif colourCheck(tweet) is not None:
            c = hex_to_rgb(colourCheck(tweet))
            blinkt.set_all(c[0], c[1], c[2], 0.4)
            blinkt.show()
            haveSetColour = True		
        else:
            twindex += 1
            if twindex >= len(tweets): haveSetColour = True
    time.sleep(10)