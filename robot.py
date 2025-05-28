#establishing class, objects, attributes, methods
class Robot:
    def __init__ (self, name, rwheel, lwheel):
        self.name = name
        #getting GPIO in sets for R and L
        self.rwheel = tuple(rwheel)
        self.lwheel = tuple(lwheel)

        #indetifying individual numbers as ints
        self.rwheel_f = int(rwheel[0])
        self.rwheel_b = int(rwheel[1])

        self.lwheel_f = int(lwheel[0])
        self.lwheel_b = int(lwheel[1])

    #methods
    def forward(self, sec):
        GPIO.output(self.rwheel_f, True)
        GPIO.output(self.lwheel_f, True)
        #stop
        time.sleep(sec)
        GPIO.output(self.rwheel_f, False)
        GPIO.output(self.lwheel_f, False)

    def backward(self, sec):
        GPIO.output(self.rwheel_b, True):
        GPIO.output(self.lwheel_b, True):
        #stop
        time.sleep(sec)
        GPIO.output(self.rwheel_b, False)
        GPIO.output(self.lwheel_b, False)

    def lturn(self, sec):
        GPIO.output(self.rhweel_f, True)
        #stop
        time.sleep(sec)
        GPIO.output(self.rwheel_f, False)

    def rturn(self, sec):
        GPIO.output(self.lwheel_f, True)
        #stop
        time.sleep(sec)
        GPIO.output(self.lwheel_f, False)

#establishing a robot object
randal = Robot("randal", (17,24), (25,26))

#print
randal.forward(3)
randal.backward(3)
randal.lturn(3)
randal.rturn(3)
exit()