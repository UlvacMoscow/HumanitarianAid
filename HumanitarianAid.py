import math

MAXIMUM_NUMBER_OF_CONTAINERS_IN_A_TRUCK = 10
MAXIMUM_BOXES_IN_THE_CONTAINER = 25


def out_all(trucks, containers, all_boxes):
    amount = 0
    for truck in range(1, trucks + 1):
        print('грузовик номер {}'.format(truck))
        for container in range(1, containers + 1):
            if amount > all_boxes:
                break
            print('контейнер номер {}'.format(container))
            for number in range(MAXIMUM_BOXES_IN_THE_CONTAINER):
                amount += 1
                if amount <= all_boxes:
                    print('ящик номер ', amount)


def get_number_of_trucks(amount):
    number_of_container = math.ceil(amount/MAXIMUM_BOXES_IN_THE_CONTAINER)
    number_of_truck = math.ceil(number_of_container/MAXIMUM_NUMBER_OF_CONTAINERS_IN_A_TRUCK)
    out_all(int(number_of_truck), MAXIMUM_NUMBER_OF_CONTAINERS_IN_A_TRUCK, int(amount))
    print('кол-во контейнеров', number_of_container)
    print('кол-во грузовиков', number_of_truck)


while True:
    try:
        boxes = int(input('введите кол-во ящиков'))
        print(boxes)
    except ValueError:
        print('введите целое число')
    get_number_of_trucks(boxes)

