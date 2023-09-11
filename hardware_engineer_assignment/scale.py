import serial
import time

ser = serial.Serial('COM3', 9600, timeout=1)

def turn_on_and_tare_scale():
    try:
        ser.write(b'ON\r\n')
        # Give the scale some time to turn on
        time.sleep(2)
        ser.write(b'TARE\r\n')
        print("Scale has been turned on and tared.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        ser.close()

turn_on_and_tare_scale()
