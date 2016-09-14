from bibliopixel.led import LEDMatrix, mapGen, MultiMapBuilder, MatrixRotation


def genDisplayParams():
    gen = MultiMapBuilder()
    gen.addRow(mapGen(25, 25, rotation=MatrixRotation.ROTATE_90, vert_flip=True))
    gen.addRow(mapGen(25, 25, rotation=MatrixRotation.ROTATE_90, vert_flip=False))

    params = {
        "width": 25,
        "height": 50,
        "coordMap": gen.map,
    }
    return params

MANIFEST = [
    {
        "id": "kilodisplay",
        "class": LEDMatrix,
        "type": "preset",
        "preset_type": "controller",
        "control_type": "matrix",
        "display": "KiloDisplay",
        "desc": "KiloDisplay 25x50",
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
                "default": 255,
                "help": "Master brightness for display, 0-255"
            }
        ],
        "preconfig": genDisplayParams
    }
]
