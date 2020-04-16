import time, sys
import os
import threading
import RPi.GPIO as GPIO
import time
import sys
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
TRIG = 18
ECHO = 24
buzzer = 3
led = 2
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
            function()
            time.sleep(2)
    def play(self):
        self._stopper.clear()


def function():
    print(" Distance Measurement in progress")
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.setup(led,GPIO.OUT)
    GPIO.setup(buzzer,GPIO.OUT)
    while True:
        GPIO.output(TRIG, False)
        time.sleep(1)
        GPIO.output(TRIG, True)
        time.sleep(0.01)
        GPIO.output(TRIG, False)
        while GPIO.input(ECHO)==0:
            pulse_start=time.time()
        while GPIO.input(ECHO)==1:
            pulse_end=time.time()
            pulse_duration=pulse_end-pulse_start
            distance = pulse_duration*11150
            distance = round(distance,2)
        if distance > 20 and distance < 60:
            GPIO.output(buzzer, GPIO.HIGH)
            GPIO.output(led, GPIO.LOW)
            print("BUZZER ON/LED OFF")
        else:
            print("BUZZER OFF/LED ON")
            GPIO.output(buzzer, GPIO.LOW)
            GPIO.output(led, GPIO.HIGH)


#t2 = PrintingThread()
#t2.start()