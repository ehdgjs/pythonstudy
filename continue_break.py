# absent = [2, 5]
# no_book = [7]
# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("교무실로 와 {0}번".format(student))
#         break
#     print("{0} 책 읽어".format(student))

# 번호 1,2,3,4 앞에 100을 붙이는 법
student = [1,2,3,4]
print(student)
student = ["100"+str(i) for i in student]
print(student)

# 글자 개수로 변환
students = ["Iron man", "Thor", "Groot"]
# students = [len(i) for i in students]
# print(students)

# 대문자로 변경
students = [i.upper() for i in students]
print(students)