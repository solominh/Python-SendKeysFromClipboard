import pyautogui
import win32clipboard
import keyboard
import time


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

hotkey = keyboard.add_hotkey(
    'ctrl+alt+shift+c,space', main, blocking=True)
recorded = keyboard.record(until='esc')
