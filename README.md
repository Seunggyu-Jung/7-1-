# 나도 코딩 파이썬: 7강  함수

# 1. 함수
- def로 표현 
```
def open_accaunt():
    print("신규 계좌를 개설합니다.") # 함수의 전달값을 정의
    
open_accaunt()
-> 신규 계좌를 개설합니다.
```

# 2. 전달값과 반환값
- 전달값: balance(잔고) , money(입금)
- 반환값: balance + money 
```
은행에 입금을 한 경우
def deposit(balance,money):   # 입금
    print("입금이 완료되었습니다. 잔액은 {0}입니다".format(balance + money))
    return balance + money # return = 반환값, 이 함수대로 계산 해준다는 것을 의미

balance = 0
balance = deposit(balance, 1000)
print(balance)
-> 입금이 완료되었습니다. 잔액은 1000입니다
-> 1000
```

```
은행에서 출금을 할 경우
def withdraw(balance,money): #출금
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance
```

```
은행에서 수수료를 납부 할 경우
def withdraw_night(balance, money): #저녁에 출금, 수수료 발생
    commission = 100 # 수수료 100원
    return commission , balance - money - commission
commission , balance = withdraw_night(balance,500)
print("수수료는 {0}원 이며, 잔액은 {1} 입니다.".format(commission, balance))
-> 수수료는 100원 이며, 잔액은 400 입니다.
```

# 3. 기본값 
- 함수 변수에 하나의 값을 고정시킨 값
- 주로 소수의 변수에만 차이를 두고 싶은 경우에 사용

```
기본값 : age, main_lang
def profile(name, age = 17, main_lang = "파이썬"):
    print("이름 :{0}\t 나이: {1} \t 언어: {2}".format(name, age, main_lang))

profile("유재석")
profile("김태호")
-> 
이름 :유재석     나이: 17        언어: 파이썬
이름 :김태호     나이: 17        언어: 파이썬
```

# 4. 키워드값 
- 매개변수의 값을 키워드로 고정시켜놓은 것, 기본값과는 차이가 있음
- 매개변수의 값이 키워드로 정해진다면, 호출시 매개변수 순서에 상관없이 함수에서 정의된 순서대로 나온다.

```
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name = "유재석", main_lang="python" , age= 20) # 호출 함수의 매개변수에 값을 키워드로 고정시킨 것
profile(age = 17, main_lang= "Java", name = "김태호")
-> 
유재석 20 python
김태호 17 Java
```

# 5. 가변인자
-  값의 범위가 정해지지 않음, 가변한다는 의미
- 가변인자는 인자 앞에 *을 붙이변서 사용
- 변수내용과 무관하게 나열할 수 있음
- end = " " -> 밑으로 내려갈 내용을 한줄로 출력한다.

```
가변인자 : *langauge
def profile(name, age, *langauge):
    print("이름 :{0}\t 나이: {1}".format(name, age), end=" ") # end = " " -> 밑으로 내려갈 내용을 한줄로 출력한다.
    for lang in langauge:
        print(lang, end =" ")
    print()
    
profile("유재석", 20, "python", "Java", "C", "C++", "C#")
profile("김태호", 17, "python" "C")

-> 
이름 :유재석     나이: 20 python Java C C++ C# 
이름 :김태호     나이: 17 pythonC
```

# 6. 지역변수와 전역변수
- 지역변수 : 함수 내에서 정의된 변수
- 전역변수(global) : 함수 외에서 정의된 변수

- 지역변수로 표현한 경우(지역변수 : gun = 20)
```
gun = 10
 def checkpint(soldiers):
    gun = 20 
    gun = gun - soldiers
    print("[함수 내에서] 남은 총 {0}자루.".format(gun))


print("전체 총 : {0}".format(gun))
checkpint(2)
print("남은 총 : {0}".format(gun))
->
전체 총 : 10
[함수 내에서] 남은 총 18자루. -> 이 값만 지역변수로 나온 값
남은 총 : 10
```

- 전역변수로 표현한 경우(전역변수 : global gun), 가급적이면 전역변수를 안씀(복잡해짐)
```
gun = 10
def checkpint(soldiers):
    global gun # 전역변수 -> 함수 외부의 변수를 끌어오는 함수, gun = 10 , 가급적이면 전역변수를 안씀(복잡해짐)
    gun = gun - soldiers
    print("[함수 내에서] 남은 총 {0}자루.".format(gun))


print("전체 총 : {0}".format(gun))
checkpint(2)
print("남은 총 : {0}".format(gun))
->
전체 총 : 10
[함수 내에서] 남은 총 8자루.
남은 총 : 8
```

- return 값으로 외부의 gun 값을 가져오는 경우 -> 전역변수처리가 아님
```
gun = 10
def checkpint_ret(gun, soldiers):   #return 값으로 외부의 gun 값을 가져오는 경우 -> 전역변수처리가 아님
    gun = gun - soldiers
    print("[함수 내에서] 남은 총 {0}자루.".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpint_ret(gun, 2)
print("남은 총 : {0}".format(gun))
->
전체 총 : 10
[함수 내에서] 남은 총 8자루.
남은 총 : 8
```



