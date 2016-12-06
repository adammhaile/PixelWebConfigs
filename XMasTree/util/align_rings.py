from init_led import setup, colors
import sys
import click
from collections import deque

# Ring Definition Here
rings = [
    [299],
    [296, 297, 298],
    [294, 295],
    [292, 293],
    [291, 290],
    [288, 289],
    [286, 287, 285],
    [280, 281, 282, 283, 284, 277, 278, 279],
    [270, 271, 272, 273, 274, 275, 276, 265, 266, 267, 268, 269],
    [256, 257, 258, 259, 260, 261, 262, 263, 264, 251, 252, 253, 254, 255],
    [241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 235, 236, 237, 238, 239, 240],
    [223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 218, 219, 220, 221, 222],
    [206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 200, 201, 202, 203, 204, 205],
    [186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 178, 179, 180, 181, 182, 183, 184, 185],
    [162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 156, 157, 158, 159, 160, 161],
    [139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 130, 131, 132, 133, 134, 135, 136, 137, 138],
    [113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 106, 107, 108, 109, 110, 111, 112],
    [87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 79, 80, 81, 82, 83, 84, 85, 86],
    [51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 42, 43, 44, 45, 46, 47, 48, 49, 50],
    [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 0, 1, 2, 3, 4, 5, 6],
]
# End Ring Definition


ring_index = 0


def fwd():
    global ring_index
    global rings
    ring = deque(rings[ring_index])
    ring.rotate(1)
    rings[ring_index] = list(ring)


def back():
    global ring_index
    global rings

    ring = deque(rings[ring_index])
    ring.rotate(-1)
    rings[ring_index] = list(ring)


def next_ring():
    global ring_index
    global rings
    if ring_index < (len(rings) - 1):
        ring_index += 1


def last_ring():
    global ring_index
    if ring_index > 0:
        ring_index -= 1


def export():
    global rings
    output = 'rings = [\n'
    for r in rings:
        output += '    {},\n'.format(r)
    output += ']\n'

    print('')
    print(output)


def exit():
    sys.exit()


funcs = {
    'j': fwd,
    'k': back,
    'n': next_ring,
    'm': last_ring,
    chr(13): export,
    chr(27): exit
}


def print_rings():
    global ring_index
    global rings
    print('')
    for ri in range(len(rings)):
        print(('*' if ri == ring_index else '') + str(rings[ri]))


def update():
    led.all_off()
    for ri in range(len(rings)):
        for i in rings[ri]:
            led.set(i, colors.Yellow if ri == ring_index else colors.Red)
        led.set(rings[ri][0], colors.Green)
        led.set(rings[ri][-1], colors.Blue)

    led.update()


def get_function():
    c = click.getchar(echo=False)
    if c not in funcs:
        print('Invalid Option: {}'.format(c))
    else:
        f = funcs[c]
        f()


def main():
    global led
    led = setup()
    update()
    while True:
        print_rings()
        get_function()
        update()


if __name__ == '__main__':
    main()
