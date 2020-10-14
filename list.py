# 리스트 []

subway = ["유재석", "조세호", "박명수"]

print(subway.index("조세호"))

subway.append("하하")
print(subway)

subway.insert(1, "정형돈")
print(subway)

# print(subway.pop())
# print(subway.pop())


subway.append("유재석")
print(subway)
print(subway.count("유재석"))

num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

num_list.clear()
print(num_list)

num_list = [5,2,4,3,1]
mix_list = ["123", True]

num_list.extend(mix_list)
print(num_list)