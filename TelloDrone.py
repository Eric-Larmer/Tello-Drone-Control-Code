import socket
import keyboard
import os
import time
import cv2, pickle, struct

class TelloDrone():

    def __init__(self,address):
        #Initialize all the variables
        self.address = address
        self.portCtrl = 8889
        self.portTele = 8890
        self.portVid = 11111
        self.droneSockCtrl = 0
        self.droneSockTele = 0
        self.droneSockVid = 0
        self.prevMsgTime = 0

        self.payload_size = struct.calcsize("Q")
        self.data = b""

        self.speed = 50
        self.forback = 0
        self.rightleft = 0
        self.updown = 0
        self.rotate = 0
        print("Drone instance intialized")

    def send(self, message, port):
        #Send Commands to Drone
        self.droneSockCtrl.sendto(message.encode('utf-8'), (self.address, port))
        #print("Sent")

    def recieve(self):
        #Recieve Commands from drone (Control Channel)
        response, ip_address = self.droneSockCtrl.recvfrom(128)
        #print("Response from drone, ",response)
        return response

    def connectToDrone(self):
        self.droneSockCtrl = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.droneSockTele = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #self.droneSockVid = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.droneSockTele.bind((socket.gethostname(),self.portTele))
        #self.droneSockVid.bind((socket.gethostname(),self.portVid))

        print("Attempting to connect..")

        message = "command"
        self.send(message, self.portCtrl)
        print(self.recieve())
        print("Taken Control of Tello...")
        self.send('streamon', self.portCtrl)
        print(self.recieve())
        print("Video Stream Active....")
        
              

    def closeConnection (self):
        self.droneSockCtrl.close()
        self.droneSockTele.close()
        print("Socket Closed")

    def droneCtrl (self):
        
        prev = [self.forback,self.rightleft,self.updown,self.rotate]

        key = keyboard.read_key()

        if key == 'w' and self.forback < 100:
            self.forback = self.speed
        elif key == 's' and self.forback > -100:
            self.forback = -self.speed
        else:
            self.forback = 0

        if key == 'a' and self.rightleft < 100:
            self.rightleft = self.speed
        elif key == 'd' and self.rightleft > -100:
            self.rightleft = -self.speed
        else:
            self.rightleft = 0

        if key == 'space' and  self.updown< 100:
            self.updown = self.speed
        elif key == 'shift' and self.updown > -100:
            self.updown = -self.speed
        else:
            self.updown = 0


        if key == 'e' and self.rotate < 100:
            self.rotate = self.speed
        elif key == 'q' and self.rotate > -100:
            self.rotate = -self.speed
        else:
            self.rotate = 0

        current = [self.forback,self.rightleft,self.updown,self.rotate]

        if (prev != current and (time.time()-self.prevMsgTime) > 0.01) or (time.time() - self.prevMsgTime) > 10:
            self.send("rc "+str(self.rightleft)+" "+str(self.forback)+" "+str(self.updown)+" "+str(self.rotate), self.portCtrl)
            self.prevMsgTime = time.time()
            #self.recieve()

         
        if key == "t":
            #print("down 20")
            self.send('takeoff',self.portCtrl)
            self.recieve()

        elif key == "l":
            #print("down 20")
            self.send('land',self.portCtrl)
            self.recieve()

        elif key == "z":
            #print("down 20")
            self.send('emergency',self.portCtrl)
            self.recieve()



    def droneTelemetry (self):
        while True:
            #os.system('cls')
            self.droneSockTele.recv(1024)

    def telloVideoStream (self):

        self.stream = cv2.VideoCapture('udp://@0.0.0.0:11111', cv2.CAP_FFMPEG)
        self.frame = None

        while True:
            self.ret, self.frame = self.stream.read()
            print(self.ret)
            if(self.ret):
                cv2.imshow('frame', self.frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        self.stream.release()
        cv2.destroyAllWindows()
        self.send('streamoff',self.portCtrl)

       


    
    
