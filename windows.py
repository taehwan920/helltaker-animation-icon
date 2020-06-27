from ctypes import windll


def onTop(win_py):
    windll.user32.SetWindowPos(win_py, -1, 0, 0, 0, 0, 0x0003)
