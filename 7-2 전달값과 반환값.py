def deposit(balance,money):   # 입금
    print("입금이 완료되었습니다. 잔액은 {0}입니다".format(balance + money))
    return balance + money # return = 반환값, 이 함수대로 계산 해준다는 것을 의미

balance = 0
balance = deposit(balance, 1000)
print(balance)

def withdraw(balance,money): #출금
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance

#balance = withdraw(balance, 500)


def withdraw_night(balance, money): #저녁에 출금, 수수료 발생
    commission = 100 # 수수료 100원
    return commission , balance - money - commission
commission , balance = withdraw_night(balance,500)
print("수수료는 {0}원 이며, 잔액은 {1} 입니다.".format(commission, balance))