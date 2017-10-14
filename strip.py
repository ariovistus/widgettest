
class SimStrip:
    def __init__(self, numLEDs, leds, globalBrightness):
        self.nleds = numLEDs
        self.leds = leds

    def clearStrip(self):
        for led in range(self.nleds):
            self.setPixel(led, 0, 0, 0)

    def setPixel(self, led_index, red, green, blue):
        if not (0 <= led_index < self.nleds):
            return

        self.leds[led_index]['red'] = red
        self.leds[led_index]['green'] = green
        self.leds[led_index]['blue'] = blue

    def show():
        self.notify_change({
            'name': 'leds', 
            'type': 'change', 
            'new': 'yo mama', 
            'old': 'yo mama',
        })
