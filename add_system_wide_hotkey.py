import keyboard


def print_something():
    print('print something')


keyboard.add_hotkey('ctrl+alt+shift+c', print_something)
recorded = keyboard.record(until='esc')
