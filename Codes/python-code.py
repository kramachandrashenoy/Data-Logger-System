import serial
import csv
arduino_port = "COM3"  
baud = 9600  
fileName = "analog-data.csv"  


try:
    ser = serial.Serial(arduino_port, baud)
    print("Connected to Arduino port: " + arduino_port)
except serial.SerialException as e:
    print(f"Error connecting to Arduino: {e}")
    exit()


sensor_data = []
samples = 10
line = 0  
while line < samples:
    getData = ser.readline()  
    dataString = getData.decode('utf-8').strip()  
    print(dataString)

    readings = dataString.split(",")  
    print(readings)

    sensor_data.append(readings)  
    print(sensor_data)

    line += 1


if not sensor_data:
    print("No data collected.")
    exit()


try:
    with open(fileName, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(sensor_data)
    print(f"Data successfully written to {fileName}")
except IOError as e:
    print(f"Error writing to CSV file: {e}")
    exit()
