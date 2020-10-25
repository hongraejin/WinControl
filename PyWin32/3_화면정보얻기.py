# 스크린의 크기와 픽셀 정보를 가지고 오기

# 스크린 해상도 얻기
from win32api import GetSystemMetrics

print("Width : ", GetSystemMetrics(0))
print("Height : ", GetSystemMetrics(1))

# 화면 픽셀 색상 얻기
import win32api
import win32gui

# 위치 x = 500, y = 500 의 위치를 16진수로 표현
color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()),500,500)
print(hex(color))

# RGB 튜플로 표현하고 싶다면

def RGBInt2RGBtuple(RGBInt):

    blue = RGBInt & 255
    green = (RGBInt >> 8) & 255
    red = (RGBInt >> 16) & 255

    return (red, green, blue)

color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), 500, 500)

print(RGBInt2RGBtuple(color))