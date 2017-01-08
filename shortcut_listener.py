import pyHook
import pythoncom


hooks_manager = pyHook.HookManager()


def OnKeyBoardEvent(event):
    return False

hooks_manager.KeyDown = OnKeyBoardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
