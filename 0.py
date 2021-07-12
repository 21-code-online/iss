#!/bin/python3

import json
import requests
from turtle import *

# https://docs.python-requests.org/en/master/
url = 'http://api.open-notify.org/astros.json'
response = requests.get(url)
result = json.loads(response.text)
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






















