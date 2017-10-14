import time

class ColorCycleTemplate:
    def __init__(self, numLEDs=144, pauseValue=0, numStepsPerCycle=100, numCycles=-1, globalBrightness=4, order='rgb'):
        self.numLEDs = numLEDs
        self.pauseValue = pauseValue
        self.numStepsPerCycle = numStepsPerCycle
        self.numCycles = numCycles
        self.globalBrightness = globalBrightness
        self.order = order
        self.strip = None
        self.repaint = False

    def init(self):
        pass

    def shutdown(self):
        pass

    def update(self):
        raise NotImplementedError("Plase implement the update() method")

    def cleanup(self):
        self.shutdown()
        self.strip.clearStrip()
        self.strip.cleanup()


    def start(self, strip):
        try:
            self.strip = strip
            self.strip.clearStrip()
            self.init()
            self.strip.show()
            currentCycle = 0
            while True:
                for currentStep in range(self.numStepsPerCycle):
                    self.repaint = False
                    self.update(currentStep, currentCycle)
                    if self.repaint:
                        self.strip.show()
                    time.sleep(self.pauseValue + 1)
                currentCycle += 1
                if self.numCycles != -1 and currentCycle >= self.numCycles:
                    break
            self.cleanup()
        except KeyboardInterrupt:
            print ("yadurp?")
            self.cleanup()

