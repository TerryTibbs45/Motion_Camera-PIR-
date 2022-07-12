from gpiozero import MotionSensor
from gpiozero import LED
from picamera import PiCamera
from datetime import datetime
from time import sleep
import time


pir = MotionSensor(26)
led = LED(13)
camera = PiCamera()
now = datetime.now() # current date and time

def clock():     
    while True:
        print("Ready")
        pir.wait_for_motion()
        print("Motion detected!")
        sleep(2)
        camera.capture('/home/User/motion_cam/test_motion.jpg')
        print(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), end="\r")
        sleep(3)
        camera.start_recording('/home/User/motion_cam/test_motion.h264')
        camera.start_preview()
        camera.resolution = (1024, 768)
        led.on()
        sleep(30)
        pir.wait_for_no_motion()
        camera.stop_preview()
        camera.stop_recording()
        led.off()
        print("lights off")
clock() 