# 1.996   0.1256    2.996   0.1256    3.496   0.1256

# xro, yro, xr1, yr1, xp, yp = map(float, input().split())

# print('Привет введи свой возраст')
# age = input()
age = 0
while age != 120:
    age = age + 1
    agelen = len(str(age))
    ageInt = int(age)


    def gg(ageInteger):
        if ageInteger in range(2, 5):
            print('Вам {0} года'.format(ageInt))

        if ageInteger in range(5, 10) or ageInteger == 0:
            print('Вам {0} лет'.format(ageInt))
        if ageInteger == 1:
            print('Вам {0} год'.format(ageInt))


    if agelen == 1:
        gg(ageInt)

    if agelen == 2:
        if ageInt in range(10, 21):
            print('Вам {0} лет'.format(ageInt))
        else:
            gg(int(ageInt % 10))

    if agelen == 3:
        if ageInt in range(105, 121):
            print('Вам {0} лет'.format(ageInt))
        else:
            gg(int(ageInt % 10))


