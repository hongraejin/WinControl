# 파일 복사
import win32api
win32api.CopyFile("test.txt","test_copied.txt")
# 없을 경우 예외 발생

# 파일 이름 변경 또는 이동
# win32api.MoveFile('test_copied.txt','test_new.txt')

# 파일 이동
# 현재위치에서 new_folder 가 이미 있어야함
# win32api.MoveFile('test_new.txt','./new_folder/test_new.txt')

# 파일 삭제
# win32api.DeleteFile('test.txt')