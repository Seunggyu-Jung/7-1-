# 키워드값 -> 매개변수의 값이 키워드로 정해진다면, 호출시 매개변수 순서에 상관없이 정의된 순서대로 나온다.

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name = "유재석", main_lang="python" , age= 20) # 호출 함수의 매개변수에 값을 키워드로 고정시킨 것
profile(age = 17, main_lang= "Java", name = "김태호")



