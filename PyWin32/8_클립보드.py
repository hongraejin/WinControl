import win32clipboard

# 클립보드에 텍스트 복사
win32clipboard.OpenClipboard()
win32clipboard.EmptyClipboard()
win32clipboard.SetClipboardText('Text to Clipboard')
win32clipboard.CloseClipboard()

# 클립보드에서 가져오기
win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

print(data)
