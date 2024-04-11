#!/usr/bin/python

import serial
import json

import time

arduino = serial.Serial(port="/dev/ttyACM0", baudrate=9600, timeout=0.1)


def read_serial():
    if arduino.in_waiting > 0:
        data = arduino.readlines().decode("utf").rstrip('\n')
        # arduino.close()
        # if len(data) > 0:
        return int(data)


if __name__ == "__main__":
    
    while True:
        x = read_serial()

        if x == 5:
            print("num5")

        elif x == 6:
            print("num6")