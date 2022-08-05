import keyboard

def droneCtrl (self):
        #fsdjklsadfj
        if keyboard.is_pressed("w"):
            #print("forward")
            self.send('forward 20',self.portCtrl)
            self.recieve()
            

        elif keyboard.is_pressed("s"):
            #print("backward")
            self.send('back 20',self.portCtrl)
            self.recieve()

        elif keyboard.is_pressed("a"):
            #print("left")
            self.send('left 20',self.portCtrl)
            self.recieve()

        elif keyboard.is_pressed("d"):
            #print("right")
            self.send('right 20',self.portCtrl)
            self.recieve()

        elif keyboard.is_pressed("q"):
            #print("rotate CCW")
            self.send('ccw 1',self.portCtrl)
            self.recieve()

        elif keyboard.is_pressed("e"):
            #print("rotate CW")
            self.send('cw 1',self.portCtrl)
            self.recieve()

        elif keyboard.is_pressed("space"):
            #print("up 20")
            self.send('up 1',self.portCtrl)
            self.recieve()

        elif keyboard.is_pressed("x"):
            #print("down 20")
            self.send('down 1',self.portCtrl)
            self.recieve()
            
        elif keyboard.is_pressed("t"):
            #print("down 20")
            self.send('takeoff',self.portCtrl)
            self.recieve()

        elif keyboard.is_pressed("l"):
            #print("down 20")
            self.send('land',self.portCtrl)
            self.recieve()

        elif keyboard.is_pressed("z"):
            #print("down 20")
            self.send('emergency',self.portCtrl)
            self.recieve()

        #else:
            #self.send('stop',self.portCtrl)
            #self.recieve()
            