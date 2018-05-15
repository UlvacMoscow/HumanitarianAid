# - Вы доставляете гуманитарную помощь в виде ящиков одинакового размера. У вас есть грузовики и контейнеры.
# В каждый грузовик влезает максимум 10 контейнеров. В каждый контейнер ­ не более 25 ящиков.
# Ящики, контейнеры и грузовики пронумерованы.
# Напишите программу, которая будет распределять ящики по контейнерам и грузовикам в зависимости от их количества,
# а также напечатает, сколько всего нужно грузовиков и контейнеров.
# На вход программы через консоль должно подаваться число ящиков.
# На выходе результат должен выглядеть следующим образом:
#
# Грузовик 1:
#
# Контейнер 1:
#
# Контейнер 2
#
# Ящик 1
#
# Ящик 2
#
# Ящик 3


MAXIMUM_NUMBER_OF_CONTAINERS_IN_A_TRUCK = 10
MAXIMUM_BOXES_IN_THE_CONTAINER = 25


def get_number_of_trucks(amount):
    number_of_container = round(amount/MAXIMUM_BOXES_IN_THE_CONTAINER, 0)
    number_of_truck = number_of_container/MAXIMUM_NUMBER_OF_CONTAINERS_IN_A_TRUCK

    print('кол-во контейнеров', number_of_container)
    print('кол-во грузовиков', number_of_truck)


while True:
    try:
        boxes = int(input('введите кол-во ящиков'))
        print(boxes)
    except ValueError:
        print('введите целое число')
    get_number_of_trucks(boxes)

