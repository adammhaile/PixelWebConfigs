from BiblioPixelAnimations.game.flappy import Flappy
from BiblioPixelAnimations.game.Snake import Snake
from BiblioPixelAnimations.game.Tetris import Tetris

try:
    from bibliopixel.win_gamepad_emu import WinGamePadEmu
except:
    pass

from bibliopixel.serial_gamepad import SerialGamePad


def genPad():
    pad = None
    try:
        pad = SerialGamePad()
    except Exception, e:
        print e
        pad = WinGamePadEmu()
    return pad


def genParams():
    return {"inputDev": genPad()}

MANIFEST = [
    {
        "id": "flappy",
        "class": Flappy,
        "type": "preset",
        "preset_type": "animation",
        "display": "Flappy Pixel",
        "desc": "Low-Res Flappy Bird Clone",
        "controller": "matrix",
        "params": [],
        "preconfig": genParams
    },
    {
        "id": "snake",
        "class": Snake,
        "type": "preset",
        "preset_type": "animation",
        "display": "Snake",
        "desc": "Snake Game",
        "controller": "matrix",
        "params": [],
        "preconfig": genParams
    },
    {
        "id": "tetris",
        "class": Tetris,
        "type": "preset",
        "preset_type": "animation",
        "display": "Tetris",
        "desc": "Low-Res Tetris Clone",
        "controller": "matrix",
        "params": [{
            "default": False,
            "help": "On for the harder, more Maniacal version.",
            "id": "evil",
            "label": "Maniacal Mode",
            "type": "bool"
        }],
        "preconfig": genParams
    }
]
