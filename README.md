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


