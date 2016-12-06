from bibliopixel.animation import BaseCircleAnim
import bibliopixel.colors as colors

class DiskBloom(BaseCircleAnim):

    def __init__(self, led, spread = 1):
        super(DiskBloom, self).__init__(led)
        self.spread = spread

    def step(self, amt = 8):
        for i in range(self.ringCount):
            c = colors.hue_helper(i, int(self.ringCount * self.spread), self._step)
            self._led.fillRing(i, c)

        self._step += amt
        if(self._step >= 255):
            self._step = 0

class Swirl(BaseCircleAnim):

    def __init__(self, led, angle=12):
        super(Swirl, self).__init__(led)
        self.angle = angle

    def step(self, amt = 1):
        for a in range(0, 360, self.angle):
            c = colors.hue_helper360(a, 360, self._step)
            for i in range(self.ringCount):
                self._led.set(i, a, c)

        self._step += amt

class ArcRotate(BaseCircleAnim):

    def __init__(self, led, colors, arc = 180, outterRing = -1):
        super(ArcRotate, self).__init__(led)
        if outterRing < 0 or outterRing > self._led.lastRing:
            outterRing = self._led.lastRing
        self.outterRing = outterRing
        self.colors = colors
        self.arcCount = len(self.colors)
        self.arc = arc/2

    def step(self, amt = 1):
        self._led.all_off()
        ci = 0
        for r in range(self.outterRing, self.outterRing - self.arcCount, -1):
            c = self.colors[ci]
            ci += 1
            self._led.fillRing(r, c, startAngle=self._step-self.arc, endAngle=self._step+self.arc)
        self._step += amt
        self._step %= 360

class PinWheel(BaseCircleAnim):

    def __init__(self, led, colors):
        super(PinWheel, self).__init__(led)
        self.colors = colors
        self.blades = len(self.colors)
        self.sepDegrees = 360.0 / self.blades

    def step(self, amt = 1):
        self._led.all_off()
        for r in range(0, self.ringCount):
            for c in range(len(self.colors)):
                self._led.fillRing(r, self.colors[c], startAngle=(self.sepDegrees*c)+self._step, endAngle=(self.sepDegrees*c)+self.sepDegrees+self._step)

        self._step += amt
        self._step %= 360

import random
class FireFlies(BaseCircleAnim):
    def __init__(self, led, colors, count = 10):
        super(FireFlies, self).__init__(led)
        self._colors = colors
        self._color_count = len(colors)
        self._count = count

    def step(self, amt = 1):
        amt = 1 #anything other than 1 would be just plain silly
        if self._step > self._led.numLEDs:
            self._step = 0

        self._led.all_off();

        for i in range(self._count):
            pixel = random.randint(0, self._led.numLEDs - 1)
            color = self._colors[random.randint(0, self._color_count - 1)]
            self._led._set_base(pixel, color)

        self._step += amt


rainbow = [colors.Red, colors.Orange, colors.Yellow, colors.Green, colors.Blue, colors.Purple]
MANIFEST = [
    {
        "class": ArcRotate,
        "controller": "circle",
        "desc": None,
        "display": "ArcRotate",
        "id": "ArcRotate",
        "params": [
            {
                "default": rainbow,
                "help": "",
                "id": "colors",
                "label": "Colors",
                "type": "multi",
                "controls": {
                    "help": None,
                    "label": "Color",
                    "type": "color"
                }
            },
            {
                "default": 180,
                "help": "Arc Angle to light up",
                "id": "arc",
                "label": "Arc Angle",
                "type": "int",
                "min": 1,
                "max": 359
            }
        ],
        "type": "animation"
    },
    {
        "class": DiskBloom,
        "controller": "circle",
        "desc": None,
        "display": "DiskBloom",
        "id": "DiskBloom",
        "params": [
            {
                "default": 1,
                "help": "",
                "id": "spread",
                "label": "Spread",
                "type": "int",
                "min":1,
                "max":32
            }
        ],
        "type": "animation"
    },
    {
        "class": FireFlies,
        "controller": "circle",
        "desc": None,
        "display": "FireFlies",
        "id": "FireFlies",
        "params": [
            {
                "default": rainbow,
                "help": "",
                "id": "colors",
                "label": "Colors",
                "type": "multi",
                "controls": {
                    "help": None,
                    "label": "Color",
                    "type": "color"
                }
            },
            {
                "default": 10,
                "help": "Total lit pixels in each frame",
                "id": "count",
                "label": "Pixel Count",
                "type": "int"
            }
        ],
        "type": "animation"
    },
    {
        "class": PinWheel,
        "controller": "circle",
        "desc": None,
        "display": "PinWheel",
        "id": "PinWheel",
        "params": [
            {
                "default": rainbow,
                "help": "",
                "id": "colors",
                "label": "Colors",
                "type": "multi",
                "controls": {
                    "help": None,
                    "label": "Color",
                    "type": "color"
                }
            }
        ],
        "type": "animation"
    },
    {
        "class": Swirl,
        "controller": "circle",
        "desc": None,
        "display": "Swirl",
        "id": "Swirl",
        "params": [
            {
                "default": 12,
                "help": "Degrees change per frame",
                "id": "angle",
                "label": "Angle Change",
                "type": "int"
            }
        ],
        "type": "animation"
    }
]
