from init_led import colors, setup
import sys
import click

led = None
rings = [[0]]
ring_index = 0
pixel_index = 0


def fwd():
    global ring_index
    global rings
    ring_index += 1
    rings[-1].append(ring_index)


def back():
    global ring_index
    global rings

    if len(rings[-1]) > 1:
        ring_index -= 1
        del rings[-1][-1]
    elif len(rings) > 1:
        ring_index -= 1
        del rings[-1]


def next_ring():
    global ring_index
    global rings
    ring_index += 1
    rings.append([ring_index])


def export():
    global rings
    rev = list(rings)
    rev.reverse()
    output = 'rings = [\n'
    for r in rev:
        output += '    {},\n'.format(r)
    output += ']\n'

    print('')
    print(output)


def exit():
    sys.exit()


funcs = {
    'j': fwd,
    'k': back,
    'l': next_ring,
    chr(13): export,
    chr(27): exit
}


def print_rings():
    global rings
    rev = list(rings)
    rev.reverse()
    print('')
    for r in rev:
        print(r)


def update():
    global led
    led.all_off()
    c = False
    for r in rings:
        for i in r:
            led.set(i, colors.Green if c else colors.Red)
        c = not c

    last = rings[-1][-1]
    led.set(last, colors.Blue)
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
