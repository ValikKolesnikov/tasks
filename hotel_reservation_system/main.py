import hotel_system
from datetime import datetime


def main():
    hotel = hotel_system.Hotel(name='Tourist', rooms=[])
    person_1 = hotel_system.Person(name='John', money=3000)
    person_2 = hotel_system.Person(name='Mike', money=3000)

    hotel.add_rooms(hotel_system.generate_rooms(count=20))
    hotel.show_price_list()
    room = hotel.get_room_by_number(number=3)
    hotel.allocate_room(person=person_1, room=room, date_start=datetime(2021, 1, 18), date_end=datetime(2021, 1, 30))
    hotel.allocate_room(person=person_2, room=room, date_start=datetime(2021, 1, 18), date_end=datetime(2021, 1, 30))
    hotel.release_room(room=room)
    hotel.allocate_room(person=person_2, room=room, date_start=datetime(2021, 1, 18), date_end=datetime(2021, 1, 30))


if __name__ == '__main__':
    main()
