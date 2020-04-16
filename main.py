
import time, sys
import os
import threading
sys.path.insert(0,'path/home/pi/Desktop/thread') 
import thread1 as t1
import thread2 as t2
#import TFLite_detection_webcam as t3


if __name__ == '__main__':
    
    thread1 = t1.PrintingThread()
    thread1.start()

    thread2 = t2.PrintingThread()
    thread2.start()
    
    
    #TFLite_detection_webcam = t3.PrintingThread()
    #TFLite_detection_webcam.start()

'''
import subprocess
from time import sleep

y=(2)
subprocess.Popen(["python3", 'TFLite_detection_webcam.py '])
sleep(y)
#subprocess.Popen(["python3", 'thread1.py'])
#sleep (y)
subprocess.Popen(["python3", 'thread2.py'])\
'''