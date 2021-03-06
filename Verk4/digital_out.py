"""
'digital_out.py'
===================================
Example of turning on and off a LED
from the Adafruit IO Python Client

Author(s): Brent Rubell, Todd Treece
"""
# Import standard python modules
import time

# import Adafruit Blinka
import digitalio
import board

# import Adafruit IO REST client.
from Adafruit_IO import Client, Feed, RequestError

# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = 'aio_WeGL209KhlSeLAmRU7VunUfd8BLX'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'BaronVonPepe'

# Create an instance of the REST client.
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

try: # if we have a 'digital' feed
    digital = aio.feeds('digital1')
except RequestError: # create a digital feed
    feed = Feed(name="digital1")
    digital = aio.create_feed(feed)
 
# led set up
led = digitalio.DigitalInOut(board.D5)
led.direction = digitalio.Direction.OUTPUT
 
 
while True:
    data = aio.receive(digital.key)
    if int(data.value) == 1:
        print('received <- ON\n')
    elif int(data.value) == 0:
        print('received <- OFF\n')
 
    # set the LED to the feed value
    led.value = int(data.value)
    # timeout so we dont flood adafruit-io with requests
    time.sleep(0.5)
