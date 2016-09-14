"""
Provides everything needed to load the control and map the display for
the WyoManiacal display, and load into PixelWeb
"""

from bibliopixel import LEDMatrix, MultiMapBuilder, mapGen
width, height = 128, 32


def genDisplayParams():
    w, h = width, height
    gen = MultiMapBuilder()
    gen.addRow(mapGen(w, h, serpentine=False))
    gen.addRow(mapGen(w, h, serpentine=False))
    gen.addRow(mapGen(w, h, serpentine=False))

    params = {
        "width": w,
        "height": h * 3,
        "coordMap": gen.map,
    }
    return params

MANIFEST = [
    {
        "id": "12k",
        "class": LEDMatrix,
        "type": "preset",
        "preset_type": "controller",
        "control_type": "matrix",
        "display": "12k",
        "desc": "12k 128x96",
        "params": [
            {
                "id": "threadedUpdate",
                "label": "Threaded Update",
                "type": "bool",
                "default": True,
                "help": "Enable to run display updates on a separate thread, which can improve speed."
            },
            {
                "id": "masterBrightness",
                "label": "Master Brightness",
                "type": "int",
                "min": 1,
                "max": 255,
                "default": 128,
                "help": "Master brightness for display, 0-255"
            }
        ],
        "preconfig": genDisplayParams
    }
]
