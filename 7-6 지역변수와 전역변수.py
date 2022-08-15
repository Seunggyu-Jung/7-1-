gun = 10 


# def checkpint(soldiers):
#    gun = 20 # 지역변수 -> 함수 내에서 값을 주는 것
#    gun = gun - soldiers
#    print("[함수 내에서] 남은 총 {0}자루.".format(gun))


#print("전체 총 : {0}".format(gun))
#checkpint(2)
#print("남은 총 : {0}".format(gun))


def checkpint(soldiers):
    global gun # 전역변수 -> 함수 외부의 변수를 끌어오는 함수, gun = 10 , 가급적이면 전역변수를 안씀(복잡해짐)
    gun = gun - soldiers
    print("[함수 내에서] 남은 총 {0}자루.".format(gun))


print("전체 총 : {0}".format(gun))
checkpint(2)
print("남은 총 : {0}".format(gun))


def checkpint_ret(gun, soldiers):   #return 값으로 외부의 gun 값을 가져오는 경우 -> 전역변수처리가 아님
    gun = gun - soldiers
    print("[함수 내에서] 남은 총 {0}자루.".format(gun))
    return gun


print("전체 총 : {0}".format(gun))
gun = checkpint_ret(gun, 2)
print("남은 총 : {0}".format(gun))


