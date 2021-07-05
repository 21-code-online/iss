#!/bin/python3

import json
import urllib.request
from turtle import *
import time

# http://open-notify.org/Open-Notify-API/
url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print(result)

screen = Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.gif')


# Tokyo
#lat = 35.689487
#lon = 139.691706

# Space Center, Houston
lat = 55.5502
lon = 37.097

done()






















