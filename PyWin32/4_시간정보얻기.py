from win32api import GetLocalTime

# 로컬 시간
print(GetLocalTime())
# (2020, 10, 0, 25, 21, 21, 4, 527)
#  연도, 월, 주의 여섯 번쨰 요일(6인경우 토요일), 일, 시, 분 , 초 , 밀리초
print(type(GetLocalTime()))

# 시스템 시간
from win32api import GetSystemTime
print(GetLocalTime())