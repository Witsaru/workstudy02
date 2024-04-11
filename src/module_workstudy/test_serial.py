import serial

arduino = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

def read_serial_data():
    data = arduino.readline().rstrip().decode('latin1')
    return [int(digit) for digit in data]

if __name__ == "__main__":
    while True:
        sensor_data = read_serial_data()
        print(sensor_data)  # แสดงข้อมูลของเซ็นเซอร์ทั้งหมด