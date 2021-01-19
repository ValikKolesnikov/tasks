import hotel_system
from datetime import datetime


def main():
    hotel = hotel_system.Hotel(name='Tourist', rooms=[])
    person_1 = hotel_system.Person(name='John', money=300000000)
    person_2 = hotel_system.Person(name='Mike', money=300000000)
    person_3 = hotel_system.Person(name='Dan', money=300000000)

    hotel.add_rooms(hotel_system.generate_rooms(count=5))
    hotel.show_price_list()
    room = hotel.get_room_by_number(number=3)
    hotel.allocate_room(person=person_1, room=room, date_start=datetime(2021, 1, 1), date_end=datetime(2021, 1, 5))
    hotel.allocate_room(person=person_2, room=room, date_start=datetime(2021, 1, 6), date_end=datetime(2021, 1, 12))
    hotel.allocate_room(person=person_3, room=room, date_start=datetime(2021, 1, 11), date_end=datetime(2021, 1, 13))
    order = room.get_order(person=person_1, date_start=datetime(2021, 1, 1), date_end=datetime(2021, 1, 5))
    hotel.release_room(room=room, order=order)
    

if __name__ == '__main__':
    main()