import random
for i in range(5):
    num = int(input("가위 바위 보? >>\n"))
    com = random.randrange(1,3)
    print(com)
    if num > 2:
        print("똑바로 해라")
    elif num == com:
        print("비김")

    elif num+1 == com or (num==2 and com==0):
        print("너 짐")
    else:
        print("꼴에 이김")

com = random.randrange(1,3)
print(com)