from hotel_system import *


def main():
    hotel = Hotel('Tourist')
    person_1 = Person('John', 3000)
    person_2 = Person('Mike', 3000)
    person_3 = Person('Dan', 5)

    hotel.add_rooms(generate_rooms(20))
    hotel.show_price_list()
    room = hotel.get_room_by_number(3)
    room_2 = hotel.get_room_by_number(3)
    hotel.allocate_room(person_1, room, 2)
    hotel.allocate_room(person_2, room, 1)
    hotel.allocate_room(person_3, room_2, 10)
    hotel.release_room(room)
    hotel.allocate_room(person_2, room, 1)


if __name__ == '__main__':
    main()
