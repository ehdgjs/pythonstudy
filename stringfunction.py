python = "Python is Amazing"

print(python.lower()) # 소문자
print(python.upper()) # 대문자
print(python[0].isupper()) # 첫번째 문자가 대문자인가?
print(len(python)) # 문자열 길이
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("A")) # find 문자가 존재하지 않는다면 -1 반환

print(python.count("n")) # count 문자가 몇번 나왔는지