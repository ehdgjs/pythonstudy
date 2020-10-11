from random import *

print(random()) # 0.0 ~ 1.0 임의의 값을 출력
print(random() * 10) # 0.0 ~ 10.0 임의의 값을 출력
print(int(random() * 10)) # 0~10 임의의 값 출력
print(int(random() * 10) + 1) # 1~11 임의의 값 출력

print(int(random() * 45) + 1) # 1~45 임의의 값 출력

print(randrange(1, 46)) # 1 ~ 45 값 출력

print(randint(1, 10)) # 1~10 값 출력