# 마우스 커서의 위치찾기, 이동시키기, 클릭, 드랙
import win32api
import win32con
# win32con 은 Win32와 관련된 상수들을 모아놓음

# 커서 위치찾기
pos = win32api.GetCursorPos()
print(pos)
print(type(pos))

# 커서 이동
to_pos = (200,200)
win32api.SetCursorPos(to_pos)

# 마우스 클릭
def mouse_click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

# mouse_click(300,300)


# 마우스 커서 영역 제한하기
# (left, top, right, bottm) 영역으로 마우스 커서 제한하기
# win32api.ClipCursor((200,200,700,700))

# 마우스 커저 제한 해제하기
win32api.ClipCursor((0,0,0,0))
win32api.ClipCursor()
