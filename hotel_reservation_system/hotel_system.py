import random
from datetime import datetime


class RoomIsNotBookableError(Exception):
    pass


class RoomIsNotExistInHotelError(Exception):
    pass


class Hotel:
    def __init__(self, name, rooms):
        self.__name = name
        self.__rooms = rooms

    @property
    def name(self):
        return self.__name

    @property
    def rooms(self):
        return self.__rooms

    @rooms.setter
    def rooms(self, rooms):
        self.__rooms = rooms

    def add_room(self, room):
        self.rooms.append(room)

    def add_rooms(self, rooms):
        self.rooms.extend(rooms)

    def release_room(self, room):
        if room in self.rooms:
            room.tenant = None
            room.release_date = None
            print(f'Room #{room.number} is free')
        else:
            raise RoomIsNotExistInHotelError()

    def show_price_list(self):
        for room in self.rooms:
            print(f'Room #{room.number}\n'
                  f'Is free: {room.is_free()}\n'
                  f'Cost: ${room.cost}/day\n')

    def get_room_by_number(self, number):
        for room in self.rooms:
            if room.number == number:
                return room
        return None

    def allocate_room(self, person, room, date_start, date_end):
        days_count = (date_end - date_start).days
        if days_count * room.cost < person.money and room in self.rooms and room.is_free():
            room.tenant = person
            room.release_date = date_end
            person.money -= days_count * room.cost
            print('Congratulations! Room is booked')
        else:
            raise RoomIsNotBookableError('You can not book this room(')


class Room:
    def __init__(self, number, cost):
        self.__number = number
        self.__cost = cost
        self.__tenant = None
        self.__release_date = None

    def is_free(self):
        if self.release_date is None:
            return True
        return self.release_date < datetime.now()

    @property
    def number(self):
        return self.__number

    @property
    def tenant(self):
        return self.__tenant

    @tenant.setter
    def tenant(self, tenant):
        self.__tenant = tenant

    @property
    def cost(self):
        return self.__cost

    @property
    def release_date(self):
        return self.__release_date

    @release_date.setter
    def release_date(self, date):
        self.__release_date = date


class Person:
    def __init__(self, name, money=100):
        self.__name = name
        self.__money = money

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, sum):
        self.__money = sum

    @property
    def name(self):
        return self.__name


def generate_rooms(count):
    rooms_prices = [10, 20, 100, 500, 1000]
    return [Room(i, random.choice(rooms_prices)) for i in range(1, count + 1)]
