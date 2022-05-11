'''
Defines arm gestures.
'''

from learm import Controller, Servo
import time

arm = Controller('USB')

# Grabber, range 1500-2500
servo1 = Servo(1, 1500, 2500)
servo2 = Servo(2)
servo3 = Servo(3)
servo4 = Servo(4)
servo5 = Servo(5)
servo6 = Servo(6)

servos = [servo2, servo3, servo4, servo5, servo6]
all_servos = [servo1, *servos]

# Set arm to home position
def home():
  for servo in servos:
    servo.position = 1500

  arm.setPosition(servos, wait=True)

# Set wave starting pose
def wave(times):
  servo2.position = 2500
  servo6.position = 500
  arm.setPosition([servo2, servo6], wait=True)

  for i in range(times):
    wave_right(500 if i == 0 else 1000)
    wave_left(1000)

# Wave right
def wave_right(duration = 1000):
  servo4.position = 1250
  servo5.position = 1750
  arm.setPosition([servo4, servo5], duration=duration, wait=True)

# Wave left
def wave_left(duration = 1000):
  servo4.position = 1750
  servo5.position = 1250
  arm.setPosition([servo4, servo5], duration=duration, wait=True)

def beckon(duration = 1000):
  servo3.position = 1500
  servo4.position = 750
  servo5.position = 1750
  arm.setPosition([servo3, servo4, servo5], duration=duration, wait=True)

  for i in range(3):
    servo3.position = 1250
    arm.setPosition([servo3], duration=500, wait=True)

    servo3.position = 2000
    arm.setPosition([servo3], duration=500, wait=True)

def open_claw():
  servo1.position = 1500
  arm.setPosition([servo1], wait=True)

def close_claw():
  servo1.position = 2500
  arm.setPosition([servo1], wait=True)

def throw():
  # Get in position
  servo3.position = 2250
  servo4.position = 2250
  servo5.position = 1300
  arm.setPosition([servo3, servo4, servo5], wait=True)

  time.sleep(1)

  # Throw!
  servo3.position = 1250
  servo4.position = 1250
  servo5.position = 1750
  arm.setPosition([servo3, servo4, servo5], duration=150)

  time.sleep(100. / 1000.)

  servo1.position = 1500
  arm.setPosition(servo1, wait=True)
