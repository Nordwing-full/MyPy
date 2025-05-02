##def menu():
##    print("""Конвертировать температуры(цельсия,кельвина,фаренгейта)[1]
##Конвертировать длинну(сантиметры,миллиметры,метры,километры)[2]
##Конвертировать время(секунды,минуты,часы)[3]
##
##ВСЕ ФОРМУЛЫ ДЛЯ РАСЧЁТОВ И КОНВЕРТАЦИИ БЫЛИ ВЗЯТЫ ИЗ ОФИЦИАЛЬНОГО КОНВЕРТЕРА Google!!!""")
##    while True:
##        choose = int(input("Введите номер для выбора раздела единицы измерения: "))
##        if choose == 1:
##            tempa()
##            break
##        elif choose == 2:
##            dlina()
##            break
##        elif choose == 3:
##            vrema()
##            break
##        elif choose > 3:
##            print("В будущем будет, выбирай из того что сейчас есть")
##            continue
##        else:
##            print("Пожалуйста, введите число от 1 до 3")
##            continue
##
##menu()
def tempa():
    print("""1.конвертировать градусы цельсия в фаренгейты
2.конвертировать градусы фарегнейта в цельсия
3.конвертировать градусы цельсия в кельвина
4.конвертировать градусы фаренгейта в кельвина
5.конвертировать градусы кельвина в фаренгейта
6.конвертировать градусы кельвина в цельсия

N-что бы вернуться к выбору раздела для единиц конвертаций""")
    while True:
        tempa = input("введите пункт для конвертации: ")
        if tempa == "N":
            menu()
        if tempa == "1":
            cels = float(input("введите количество градусов цельсия: "))
            result = (cels * 9/5) + 32
            print(f"{result} градусов фаренгейта")
        if tempa == "2":
            faren = float(input("введите количество градусов фаренгейта: "))
            result = 5/9 * (faren - 32)
            print(f"{result} градусов цельсия")
        if tempa == "3":
            cels = float(input("введите количество градусов цельсия: "))
            result = cels + 273.15
            print(f"{result} градусов кельвина")
        if tempa == "4":
            faren = float(input("введите количество градусов фаренгейта: "))
            result = (faren - 32) * 5/9 + 273.15
            print(f"{result} градусов кельвина")
        if tempa == "5":
            kel = float(input("введите количество градусов кельвина: "))
            result = (kel - 273.15) * 9/5 + 32
            print(f"{result} градусов фаренгейта")
        if tempa == "6":
            kel = float(input("введите количество градусов кельвина: "))
            result = kel - 273.15
            print(f"{result} градусов цельсия")

def dlina():
    print("""1.конвертировать сантиметры в миллиметры
2.конвертировать сантиметры в метры
3.конвертировать сантиметры в километры
4.конвертировать миллиметры в сантиметры
5.конвертировать миллиметры в метры
6.конвертировать миллиметры в километры
7.конвертировать метры в миллиметры
8.конвертировать метры в сантиметры
9.конвертировать метры в километры
10.конвертировать километры в миллиметры
11.конвертировать километры в сантиметры
12.конвертировать километры в метры

N-что бы вернуться к выбору раздела для единиц конвертаций""")
    while True:
        dlina = input("введите пункт для конвертации: ")
        if dlina == "N":
            menu()
        if dlina == "1":
            lenght = float(input("введите длинну в сантиметрах: "))
            result = lenght * 10
            print(f"{result} миллиметров")
        if dlina == "2":
            lenght = float(input("введите длинну в сантиметрах: "))
            result = lenght / 100
            print(f"{result} метров")
        if dlina == "3":
            lenght = float(input("введите длинну в сантиметрах: "))
            result = lenght / 100000
            print(f"{result} километров")
        if dlina == "4":
            lenght = float(input("введите длинну в миллиметрах: "))
            result = lenght / 10
            print(f"{result} сантиметров")
        if dlina == "5":
            lenght = float(input("введите длинну в миллиметрах: "))
            result = lenght / 1000
            print(f"{result} метров")
        if dlina == "6":
            lenght = float(input("введите длинну в миллиметрах: "))
            result = lenght / 1e+6
            print(f"{result} километров")
        if dlina == "7":
            lenght = float(input("введите длинну в метрах: "))
            result = lenght * 1000
            print(f"{result} миллиметров")
        if dlina == "8":
            lenght = float(input("введите длинну в метрах: "))
            result = lenght * 100
            print(f"{result} сантиметров")
        if dlina == "9":
            lenght = float(input("введите длинну в метрах: "))
            result = lenght / 1000
            print(f"{result} километров")
        if dlina == "10":
            lenght = float(input("введите длинну в километрах: "))
            result = lenght * 1e+6
            print(f"{result} миллиметров")
        if dlina == "11":
            lenght = float(input("введите длинну в километрах: "))
            result = lenght * 100000
            print(f"{result} сантиметров")
        if dlina == "12":
            lenght = float(input("введите длинну в километрах: "))
            result = lenght * 1000
            print(f"{result} метров")

def vrema():
    print("""1.конвертировать секунды в минуты
2.конвертировать секунды в часы
3.конвертировать минуты в секунды
4.конвертировать минуты в часы
5.конвертировать часы в секунды
6.конвертировать часы в минуты

N-что бы вернуться к выбору раздела для единиц конвертаций""")
    while True:
        vrema = input("введите пункт для конвертации: ")
        if vrema == "N":
            menu()
        if vrema == "1":
            time = float(input("введите время в секундах: "))
            result = time / 60
            print(f"{result} минут")
        if vrema == "2":
            time = float(input("введите время в секундах: "))
            result = time / 3600
            print(f"{result} часов")
        if vrema == "3":
            time = float(input("введите время в минутах: "))
            result = time * 60
            print(f"{result} секунд")
        if vrema == "4":
            time = float(input("введите время в минутах: "))
            result = time / 60
            print(f"{result} часов")
        if vrema == "5":
            time = float(input("введите время в часах: "))
            result = time * 3600
            print(f"{result} секунд")
        if vrema == "6":
            time = float(input("введите время в часах: "))
            result = time * 60
            print(f"{result} минут")

def menu():
    print("""Конвертировать температуры(цельсия,кельвина,фаренгейта)[1]
Конвертировать длинну(сантиметры,миллиметры,метры,километры)[2]
Конвертировать время(секунды,минуты,часы)[3]

ВСЕ ФОРМУЛЫ ДЛЯ РАСЧЁТОВ И КОНВЕРТАЦИИ БЫЛИ ВЗЯТЫ ИЗ ОФИЦИАЛЬНОГО КОНВЕРТЕРА Google!!!""")
    while True:
        choose = input("Введите номер для выбора раздела единицы измерения: ")
        if choose == "1":
            tempa()
            break
        elif choose == "2":
            dlina()
            break
        elif choose == "3":
            vrema()
            break
        elif choose > "3":
            print("В будущем будет, выбирай из того что сейчас есть")
            continue
        else:
            print("Пожалуйста, введите число от 1 до 3")
            continue

menu()

##while True:
##    menu()
##    choose = int(input("Введите номер для выбора раздела единицы измерения: "))
##    if choose == 1:
##        tempa()
##        break
##    elif choose == 2:
##        dlina()
##        break
##    elif choose == 3:
##        vrema()
##        break
##    elif choose > 3:
##        print("В будущем будет, выбирай из того что сейчас есть")
##        continue
##    else:
##        print("Пожалуйста, введите число от 1 до 3")
##        continue
