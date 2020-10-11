# jumin = "990101-1234567"

# print("성별: " + str(jumin[7]))
# print("연: " + str(jumin[:2]))
# print("월일: " + str(jumin[2:6]))

# print("뒷자리: " + str(jumin[7:]))
# print("뒷자리: " + str(jumin[-7:]))

# 문자열 포맷

print("나는 %d살 입니다." % 12)
print("나는 %s를 좋아합니다." % "파이썬")
print("%s %s" % ("a", "b"))

print("나는 {}살입니다." .format(20))
print("{} {}" .format("a", "b"))
print("{0} {1}" .format("a", "b"))
print("{1} {0}" .format("a", "b"))

print("나는 {age}살이며, {color}색을 좋아해요" .format(age = 20 , color = "빨간"))

age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")