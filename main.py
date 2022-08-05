import droneClass as drone
import keyboard
import sys
import threading



droneIP = '192.168.10.1'

drones = drone.TelloDrone(droneIP)
drones.connectToDrone() 

telemetryThread = threading.Thread(target=drones.droneTelemetry) 
telemetryThread.start()

videoStreamThread = threading.Thread(target=drones.telloVideoStream)
videoStreamThread.daemon = True
videoStreamThread.start()

while not keyboard.is_pressed('esc'):                                                        

    drones.droneCtrl()

telemetryThread.join()
videoStreamThread.join()

drones.closeConnection()                