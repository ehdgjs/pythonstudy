# 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# http://naver.com
# 규칙 1 : http:// 부분은 제외
# 규칙 2 : 처음 만나는 점 (.) 이후 부분은 제외 
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성

url = "http://naver.com"
url = url[7:]
slicingDot = url.find(".")
url = url[:slicingDot]

print(url[:3]+str(len(url))+str(url.count("e"))+"!")