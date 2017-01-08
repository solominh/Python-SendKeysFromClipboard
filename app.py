import pyautogui
import win32clipboard
import keyboard
import datetime


def read_clipboard():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    print(data)
    return data


def send_keys(data):
    pyautogui.typewrite(data.strip())


def main():
    global hotkey
    data = read_clipboard()
    send_keys(data)
    print('Send keys successfully!')

last_time_pressed = datetime.datetime.now()


def handle_hotkey():
    global last_time_pressed
    now = datetime.datetime.now()
    delta = now - last_time_pressed
    if delta.total_seconds() > 3:
        main()
        last_time_pressed = now


hotkey = keyboard.add_hotkey(
    'ctrl+alt+shift+k,Home', handle_hotkey, blocking=True, timeout=3)
recorded = keyboard.record(until='esc')
