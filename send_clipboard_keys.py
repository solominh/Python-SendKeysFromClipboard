import pyautogui
import win32clipboard


def read_clipboard():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    print(data)
    return data


def send_keys(data):
    pyautogui.typewrite(data.strip())


def main():
    data = read_clipboard()
    send_keys(data)
    print('Send keys successfully!')
