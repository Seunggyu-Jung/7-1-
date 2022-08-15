#가변인자 -> * : 값의 범위가 정해지지 않음, 가변한다는 의미
def profile(name, age, *langauge):
    print("이름 :{0}\t 나이: {1}".format(name, age), end=" ") # end = " " -> 밑으로 내려갈 내용을 한줄로 출력한다.
    for lang in langauge:
        print(lang, end =" ")
    print()
    
profile("유재석", 20, "python", "Java", "C", "C++", "C#")
profile("김태호", 17, "python" "C")