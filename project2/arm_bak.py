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
def ready_to_go():
  servo6.position = rad_to_servo(0)
  servo5.position = rad_to_servo(0.76)
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

if __name__ == '__main__':
  ready_to_go()

  '''
  time.sleep(1)
  spin_to(0)
  into_position()

  time.sleep(1)

  ready_to_go()
  time.sleep(1)
  spin_to(1)
  into_position()

  time.sleep(1)

  ready_to_go()
  time.sleep(1)
  spin_to(-1)
  into_position()
  '''

  pos = -1

  ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
  ser.reset_input_buffer()
  while True:
    #ser.reset_input_buffer()
    if ser.in_waiting > 0:
      line = ser.readline().decode('utf-8').strip()
      print(line)

      if line == 'Next' and pos < 2:
          spin_to(pos)
          into_position()
          time.sleep(1)
          ready_to_go()

          pos += 1

          ser.reset_input_buffer()

  #button.wait_for_press()
  #into_position()
  #time.sleep(1)
  #ready_to_go()
