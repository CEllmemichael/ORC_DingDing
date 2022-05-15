import ctypes

class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_ulong),
                ("y", ctypes.c_ulong)]

def get_pos():
    point = Point()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(point))
    return point.x, point.y

while 1:
    print(get_pos())