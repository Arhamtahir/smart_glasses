import time, sys
import os
import threading
import time

import board
import busio
import sys
import adafruit_gps
import paho.mqtt.publish as publish
import serial

class PrintingThread(threading.Thread):

    def __init__(self, *args, **kwargs):
        super(PrintingThread, self).__init__(*args, **kwargs)
        self._stopper = threading.Event()

    def stop(self):
        self._stopper.set()

    def stopped(self):
        return self._stopper.isSet()

    def run(self):
        while True:
            if self.stopped():
                return
            function1()
            time.sleep(2)

    def play(self):
        self._stopper.clear()

def function1():
    uart = serial.Serial(port='/dev/ttyAMA0', baudrate=9600, timeout=3000)
# Create a GPS module instance.
    gps = adafruit_gps.GPS(uart, debug=False)     # Use UART/pyserial

# Turn on the basic GGA and RMC info (what you typically want)
    gps.send_command(b'PMTK314,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')

# Set update rate to once a second (1hz) which is what you typically want.
    gps.send_command(b'PMTK220,1000')

# Main loop runs forever printing the location, etc. every second.
    last_print = time.monotonic()
    while True:
        gps.update()
        current = time.monotonic()
        if current - last_print >= 2.0:
            last_print = current
            if not gps.has_fix:
                print('Waiting for fix...')
                continue
            lat = str(gps.latitude)
            long = str(gps.longitude)
            publish.single("123",lat+":"+long, hostname="mqtt.gq",auth={'username':"navaid", 'password':"connect123@"})
            print('Latitude: {0:.6f} degrees'.format(gps.latitude))
            print('Longitude: {0:.6f} degrees'.format(gps.longitude))
 

t1 = PrintingThread()
t1.start()
