# 기본값 -> 함수의 변수에 하나의 값을 고정시켜 넣는 값

def profile(name, age = 17, main_lang = "파이썬"):
    print("이름 :{0}\t 나이: {1} \t 언어: {2}".format(name, age, main_lang))

profile("유재석")
profile("김태호")






