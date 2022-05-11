'''
Starts threads for vision and arm control, and facilitates communication between them.
'''

import threading
import time
import logging
import vision
import robot
import argparse

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

def init_arm():
    robot.home()
    robot.open_claw()
    time.sleep(2)
    robot.close_claw()

def perform_routine():
    print("callback!")

    robot.wave(2)
    robot.home()
    robot.beckon()
    robot.home()

    robot.throw()

    time.sleep(2)

    init_arm()


def wait_for_event(e):
    init_arm()

    while True:
        event_is_set = e.wait()
        logging.debug('event set: %s', event_is_set)

        perform_routine()
        e.clear()


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--prototxt", default="MobileNetSSD_deploy.prototxt",
        help="path to Caffe 'deploy' prototxt file")
    ap.add_argument("-m", "--model", default="MobileNetSSD_deploy.caffemodel",
        help="path to Caffe pre-trained model")
    ap.add_argument("-c", "--confidence", type=float, default=0.5,
        help="minimum probability to filter weak detections")
    ap.add_argument("-s", "--source", default=0)
    args = vars(ap.parse_args())

    e = threading.Event()
    t1 = threading.Thread(name='Robot', target=wait_for_event, args=(e,))
    t1.start()

    vision.start(args["prototxt"], args["model"], args["source"], args["confidence"], lambda: e.set())
