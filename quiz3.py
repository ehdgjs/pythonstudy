def std_weight(height, gender):
    height = height/100
    if gender == "남자":
        return height * height * 22
    elif gender == "여자":
        return height * height * 21

height = int(input())
gender = input()
avg_weight = round(std_weight(height, gender), 2)
print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height, gender, avg_weight))
