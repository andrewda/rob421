from learm import Controller, Servo
import time
import serial

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

def rad_to_servo(position):
  value = position  # radians [-1.57, 1.57]
  value /= 1.57  # convert [-1, 1]
  value *= 1000  # convert [-1000, 1000]
  value += 1500  # convert [500, 2500]
  return int(value)  # truncate decimals so library operates correctly

# Set arm to home position
def home():
  servo6.position = rad_to_servo(0)
  servo5.position = rad_to_servo(0.35)
  servo4.position = rad_to_servo(-1.57)
  servo3.position = rad_to_servo(0.22)
  servo2.position = rad_to_servo(0.00)
  servo1.position = 1500

  arm.setPosition([servo6, servo5, servo4, servo3, servo2, servo1], wait=True)

# Set arm to home position
def into_position():
  servo5.position = rad_to_servo(1.42)
  servo4.position = rad_to_servo(-0.68)
  servo3.position = rad_to_servo(0.55)
  servo2.position = rad_to_servo(0.00)

  arm.setPosition([servo5, servo4, servo3, servo2], wait=True)

def spin_to(position):
  servo6.position = rad_to_servo(0 + 0.5 * position)

  arm.setPosition([servo6], wait=True)


# Bread
def get_bread():
  servo6.position = rad_to_servo(-0.5)
  arm.setPosition([servo6], wait=True)

  servo5

def reset():
  servo6.position = rad_to_servo(0)
  servo5.position = rad_to_servo(0)
  arm.setPosition([servo6, servo5], wait=True)

  servo4.position = rad_to_servo(0)
  servo3.position = rad_to_servo(0)
  servo2.position = rad_to_servo(0)
  servo1.position = 1500
  arm.setPosition([servo4, servo3, servo2, servo1], wait=True)


def get_peanut_butter():
  '''
  18.5cm directly in front
  '''

  servo6.position = rad_to_servo(0)
  arm.setPosition([servo6], wait=True)

  # part1
  servo5.position = rad_to_servo(0.35)
  servo4.position = rad_to_servo(-1.57)
  servo3.position = rad_to_servo(0.22)
  servo2.position = rad_to_servo(0.00)
  servo1.position = 1500

  arm.setPosition([servo6, servo5, servo4, servo3, servo2, servo1], wait=True)

  time.sleep(1)

  #part2
  servo5.position = rad_to_servo(0.35 + 0.35)
  servo4.position = rad_to_servo(-1.57 + 0.35 * 2)
  servo1.position = 2000

  arm.setPosition([servo5, servo4, servo1], wait=True)

def get_jelly():
  '''
  19cm in front of left screw 1
  '''

  servo6.position = rad_to_servo(0.85)
  arm.setPosition([servo6], wait=True)

  # part1
  servo5.position = rad_to_servo(0.475)
  servo4.position = rad_to_servo(-1.57)
  servo3.position = rad_to_servo(0.1)
  servo2.position = rad_to_servo(0.00)
  servo1.position = 1500

  arm.setPosition([servo5, servo4, servo3, servo2, servo1], wait=True)

  time.sleep(1)

  #part2
  servo5.position = rad_to_servo(0.475 + 0.35)
  servo4.position = rad_to_servo(-1.57 + 0.35 * 2)
  servo1.position = 2000

  arm.setPosition([servo5, servo4, servo1], wait=True)

def get_knife():
  '''
  13cm in front of left screw 2
  '''

  servo6.position = rad_to_servo(1.57)
  arm.setPosition([servo6], wait=True)

  # part1
  servo5.position = rad_to_servo(-0.45)
  servo4.position = rad_to_servo(-1.57)
  servo3.position = rad_to_servo(-0.8)
  servo2.position = rad_to_servo(0.00)
  servo1.position = 2000

  arm.setPosition([servo5, servo4, servo3, servo2, servo1], wait=True)

  #part2
  # servo5.position = rad_to_servo(0.475 + 0.35)
  # servo4.position = rad_to_servo(-1.57 + 0.35 * 2)
  servo1.position = 2500
  arm.setPosition([servo1], wait=True)

  time.sleep(1)

  servo5.position = rad_to_servo(-1.57)
  arm.setPosition([servo5], wait=True)

  servo6.position = rad_to_servo(0)
  servo5.position = rad_to_servo(0.79)
  servo4.position = rad_to_servo(0)
  servo3.position = rad_to_servo(-0.79)
  servo2.position = rad_to_servo(0)
  arm.setPosition([servo6, servo5, servo4, servo3, servo2], wait=True)

  time.sleep(1)

  servo1.position = 1500
  arm.setPosition([servo1], wait=True)


if __name__ == '__main__':
  # reset()
  # # time.sleep(1)
  # get_peanut_butter()
  time.sleep(10)
  # reset()
  # get_knife()
  reset()
  # # time.sleep(1)
  get_jelly()
  # time.sleep(1)
  reset()
  # get_knife()
  # reset()





  # reset()

  # pos = 0

  # ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
  # ser.reset_input_buffer()
  # while True:
  #   #ser.reset_input_buffer()
  #   if ser.in_waiting > 0:
  #     line = ser.readline().decode('utf-8').strip()
  #     print(line)

  #     if line == 'Next':
  #       if pos == 1:
  #         get_peanut_butter()
  #         reset()
  #         get_knife()
  #         reset()
  #       elif pos == 2:
  #         get_jelly()
  #         reset()

  #       pos += 1

  #       ser.reset_input_buffer()
