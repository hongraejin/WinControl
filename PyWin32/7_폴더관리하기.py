import win32file

# 폴더 생성하기
# win32file.CreateDirectory('new_folder_2',None)

# 폴더 삭제하기
# win32file.RemoveDirectory('new_folder_2')

# 현재 경로 설정하기
win32file.CreateDirectory('upper_folder',None)
win32file.SetCurrentDirectory('upper_folder')
win32file.CreateDirectory('new_folder',None)