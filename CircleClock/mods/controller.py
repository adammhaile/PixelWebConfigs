from bibliopixel import LEDCircle


def genDisplayParams():
    rings = [
        [254, 254],  # 0 - Center point
        [248, 253],  # 1
        [236, 247],  # 2
        [216, 235],  # 3
        [192, 215],  # 4
        [164, 191],  # 5
        [132, 163],  # 6
        [92, 131],   # 7
        [48, 91],    # 8
        [0, 47],     # 9 - Outer-most ring
    ]

    params = {
        "rings": rings
    }
    return params


MANIFEST = [
    {
        "id": "controller.adammhaile.CircleClock",
        "class": LEDCircle,
        "type": "preset",
        "preset_type": "controller",
        "control_type": "circle",
        "display": "Circle Clock",
        "desc": "Adafruit DotStar Disc Display",
        "params": [
            {
                "id": "threadedUpdate",
                "label": "Threaded Update",
                "type": "bool",
                "default": True,
                "help": "Enable to run display updates on a separate thread, which can improve speed."
            }, {
                "id": "maxAngleDiff",
                "label": "Max Angle Dif",
                "type": "int",
                "min": 0,
                "max": 359,
                "default": 0,
                "help": "Maximum Angle Deviation"
            }, {
                "id": "rotation",
                "label": "Rotation",
                "type": "int",
                "min": 0,
                "max": 359,
                "default": 0,
                "help": "Angle to rotate display"
            }, {
                "id": "masterBrightness",
                "label": "Master Brightness",
                "type": "int",
                "min": 1,
                "max": 255,
                "default": 255,
                "help": "Master brightness for display, 0-255"
            }
        ],
        "preconfig": genDisplayParams
    }
]
