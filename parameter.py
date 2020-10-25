# 가변인자 매개변수의 수를 원하는대로 삽입할수 있다.
def a(*lan):
    for lang in lan:
        print(lang)

a("wr", "23")

