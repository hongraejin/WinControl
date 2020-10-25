from win32api import GetComputerName
from win32api import GetUserName

# 컴퓨터 이름
print(GetComputerName())

# 사용자 이름
print(GetUserName())