# while
customer = "토르"

index = 5
while index >= 1:
    print("{0} 커피 준비 완료했습니다. {1} 번 남았어요".format(customer, index))
    index -= 1
    if index == 0:
        print("커피 버렸다")