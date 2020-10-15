# 사전
# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet.get(5)) # None
# print(cabinet.get(5, "사용가능")) # 사용가능

# print(3 in cabinet) # True
# print(5 in cabinet) # False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])

cabinet["A-3"] = "김종국"
cabinet["C-2"] = "조세호"

del cabinet["A-3"]
print(cabinet)
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

cabinet.clear()
print(cabinet)