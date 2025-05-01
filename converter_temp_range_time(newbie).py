print("""1.конвертировать градусы цельсия в фаренгейты
2.конвертировать градусы фарегнейта в цельсия
3.конвертировать градусы цельсия в кельвина
4.конвертировать градусы фаренгейта в кельвина
5.конвертировать градусы кельвина в фаренгейта
6.конвертировать градусы кельвина в цельсия
7.конвертировать сантиметры в миллиметры
8.конвертировать сантиметры в метры
9.конвертировать сантиметры в километры
10.конвертировать миллиметры в сантиметры
11.конвертировать миллиметры в метры
12.конвертировать миллиметры в километры
13.конвертировать метры в миллиметры
14.конвертировать метры в сантиметры
15.конвертировать метры в километры
16.конвертировать километры в миллиметры
17.конвертировать километры в сантиметры
18.конвертировать километры в метры
19.конвертировать секунды в минуты
20.конвертировать секунды в часы
21.конвертировать минуты в секунды
22.конвертировать минуты в часы
23.конвертировать часы в секунды
24.конвертировать часы в минуты""")
choose = int(input("Введите номер для выбора конвертации единицы измерения: "))

if choose == 1:
    cels = float(input("введите количество градусов цельсия: "))
    result = (cels * 9/5) + 32
    print(f"{result} градусов фаренгейта")

if choose == 2:
    faren = float(input("введите количество градусов фаренгейта: "))
    result = 5/9 * (faren - 32)
    print(f"{result} градусов цельсия")

if choose == 3:
    cels = float(input("введите количество градусов цельсия: "))
    result = cels + 273.15
    print(f"{result} градусов кельвина")

if choose == 4:
    faren = float(input("введите количество градусов фаренгейта: "))
    result = (faren - 32) * 5/9 + 273.15
    print(f"{result} градусов кельвина")

if choose == 5:
    kel = float(input("введите количество градусов кельвина: "))
    result = (kel - 273.15) * 9/5 + 32
    print(f"{result} градусов фаренгейта")

if choose == 6:
    kel = float(input("введите количество градусов кельвина: "))
    result = kel - 273.15
    print(f"{result} градусов цельсия")

if choose == 7:
    lenght = float(input("введите длинну в сантиметрах: "))
    result = lenght * 10
    print(f"{result} миллиметров")

if choose == 8:
    lenght = float(input("введите длинну в сантиметрах: "))
    result = lenght / 100
    print(f"{result} метров")

if choose == 9:
    lenght = float(input("введите длинну в сантиметрах: "))
    result = lenght / 100000
    print(f"{result} километров")

if choose == 10:
    lenght = float(input("введите длинну в миллиметрах: "))
    result = lenght / 10
    print(f"{result} сантиметров")

if choose == 11:
    lenght = float(input("введите длинну в миллиметрах: "))
    result = lenght / 1000
    print(f"{result} метров")

if choose == 12:
    lenght = float(input("введите длинну в миллиметрах: "))
    result = lenght / 1e+6
    print(f"{result} километров")

if choose == 13:
    lenght = float(input("введите длинну в метрах: "))
    result = lenght * 1000
    print(f"{result} миллиметров")

if choose == 14:
    lenght = float(input("введите длинну в метрах: "))
    result = lenght * 100
    print(f"{result} сантиметров")

if choose == 15:
    lenght = float(input("введите длинну в метрах: "))
    result = lenght / 1000
    print(f"{result} километров")

if choose == 16:
    lenght = float(input("введите длинну в километрах: "))
    result = lenght * 1e+6
    print(f"{result} миллиметров")

if choose == 17:
    lenght = float(input("введите длинну в километрах: "))
    result = lenght * 100000
    print(f"{result} сантиметров")

if choose == 18:
    lenght = float(input("введите длинну в километрах: "))
    result = lenght * 1000
    print(f"{result} метров")

if choose == 19:
    time = float(input("введите время в секундах: "))
    result = time / 60
    print(f"{result} минут")

if choose == 20:
    time = float(input("введите время в секундах: "))
    result = time / 3600
    print(f"{result} часов")

if choose == 21:
    time = float(input("введите время в минутах: "))
    result = time * 60
    print(f"{result} секунд")

if choose == 22:
    time = float(input("введите время в минутах: "))
    result = time / 60
    print(f"{result} часов")

if choose == 23:
    time = float(input("введите время в часах: "))
    result = time * 3600
    print(f"{result} секунд")

if choose == 24:
    time = float(input("введите время в часах: "))
    result = time * 60
    print(f"{result} минут")
