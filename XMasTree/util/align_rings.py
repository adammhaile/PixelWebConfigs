from init_led import setup, colors
import sys
import click
from collections import deque

# Ring Definition Here
rings = [
    [28],
    [26, 27],
    [23, 24, 25],
    [19, 20, 21, 22],
    [14, 15, 16, 17, 18],
    [8, 9, 10, 11, 12, 13],
    [0, 1, 2, 3, 4, 5, 6, 7],
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
        output += '    {}\n'.format(r)
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
