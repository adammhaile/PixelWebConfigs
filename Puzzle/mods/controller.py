"""
Provides everything needed to load the control and map the display for
the WyoManiacal display, and load into PixelWeb
"""

from bibliopixel import LEDMatrix, MultiMapBuilder, mapGen, MatrixRotation
width, height = 8, 8
p_w, p_h = 3, 3
rotation = MatrixRotation.ROTATE_0


def genDisplayParams():
    gen = MultiMapBuilder()
    for _ in range(p_h):
        maps = []
        for _ in range(p_w):
            maps.append(mapGen(width, height, rotation=rotation))
        gen.addRow(*maps)

    params = {
        "width": width * p_w,
        "height": height * p_h,
        "coordMap": gen.map,
    }
    return params


MANIFEST = [
    {
        "id": "Puzzle",
        "class": LEDMatrix,
        "type": "preset",
        "preset_type": "controller",
        "control_type": "matrix",
        "display": "Ultim8x8 Puzzle",
        "desc": "Ultim8x8 Puzzle",
        "params": [
            {
                "id": "threadedUpdate",
                "label": "Threaded Update",
                "type": "bool",
                "default": False,
                "help": "Enable to run display updates on a separate thread."
            },
            {
                "id": "masterBrightness",
                "label": "Master Brightness",
                "type": "int",
                "min": 1,
                "max": 255,
                "default": 64,
                "help": "Master brightness for display, 0-255"
            }
        ],
        "preconfig": genDisplayParams
    }
]
