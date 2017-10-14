import ipywidgets as widgets
from traitlets import Unicode, Int, List, Dict, validate, observe


def init_list(n):
    result = []
    for i in range(n):
        result.append({
            'red': 0,
            'green': 255,
            'blue': 0,
            'brightness': 0,
        })
    return result


class HelloWidget(widgets.DOMWidget):
    _view_name = Unicode('HelloView').tag(sync=True)
    _view_module = Unicode("hello").tag(sync=True)
    value = Unicode('red').tag(sync=True)
    nleds = Int(144).tag(sync=True)
    leds = List(trait=Dict(), default_value=init_list(144)).tag(sync=True)

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

    def start(self, cycle):
        cycle.start(self)
