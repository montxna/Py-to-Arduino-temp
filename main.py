import wmi
import subprocess
import serial
import time


arduinoData=serial.Serial('com5',115200, timeout=2)

DETACHED_PROCESS = 8

CPUTemp = ""
GPUTemp = ""

temp = {
     "CPU Package" : "",
     "GPU Core" : ""
}

while True:
     w = wmi.WMI(namespace="root\OpenHardwareMonitor")
     temperature_infos = w.Sensor()
     for sensor in temperature_infos:
         if sensor.SensorType == u'Temperature':
             temp[sensor.Name] = str(sensor.Value)



     payload = "C " + temp["CPU Package"] + "\r"
     print(payload)
     print(payload.split())
     # cmd = str(sensor.Value)
     # cmd = cmd + '\r'
     arduinoData.write(payload.encode())
     arduinoData.flush()
     payload = "G " + temp["GPU Core"] + "\r"
     arduinoData.write(payload.encode())
     arduinoData.flush()
     time.sleep(1)

     # print (cmd)