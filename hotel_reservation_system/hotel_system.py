import random
from datetime import datetime


class RoomIsNotBookableError(Exception):
    pass


class RoomDoesNotExistInHotelError(Exception):
    pass

class OrderDoesNotExistError(Exception):
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

    def release_room(self, room, order):
        if room in self.rooms:
            room.orders.remove(order)
            print(f'{order.person.name} is gone room #{room.number}')
        else:
            raise RoomDoesNotExistInHotelError()

    def show_price_list(self):
        for room in self.rooms:
            print(f'Room #{room.number}\n'
                  f'Cost: ${room.cost}/day\n')

    def get_room_by_number(self, number):
        for room in self.rooms:
            if room.number == number:
                return room
        return None

    def can_allocate_room(self, person, room, days_count, date_start, date_end):
        return days_count * room.cost <= person.money and room in self.rooms and room.is_free(date_start, date_end)

    def allocate_room(self, person, room, date_start, date_end):
        days_count = (date_end - date_start).days
        if self.can_allocate_room(person, room, days_count, date_start, date_end):
            person.money -= days_count * room.cost
            room.orders.append(Order(person=person, date_start=date_start, date_end=date_end))
            print(f'Congratulations! Room #{room.number} is booked by {person.name}\n'
                  f'From {date_start} to {date_end}')
        else:
            raise RoomIsNotBookableError(f'You can not book room #{room.number}')


class Room:
    def __init__(self, number, cost):
        self.__number = number
        self.__cost = cost
        self.__orders = []

    @property
    def orders(self):
        return self.__orders

    @orders.setter
    def orders(self, orders):
        self.__orders = orders

    @property
    def number(self):
        return self.__number

    @property
    def cost(self):
        return self.__cost

    def is_date_between(self, date, date_start, date_end):
        return date_start <= date <= date_end

    def is_free(self, date_start, date_end):
        for order in self.orders:
            if self.is_date_between(date_start, order.date_start, order.date_end) or self.is_date_between(date_end,
                                                                                                          order.date_start,
                                                                                                          order.date_end):
                return False
        return True

    def get_order(self, person, date_start, date_end):
        for order in self.orders:
            if order.person == person and order.date_start == date_start and order.date_end == date_end:
                return order
            raise OrderDoesNotExistError()
    


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


class Order:
    def __init__(self, person, date_start, date_end):
        self.__person = person
        self.__date_start = date_start
        self.__date_end = date_end

    @property
    def person(self):
        return self.__person

    @person.setter
    def person(self, person):
        self.__person = person

    @property
    def date_start(self):
        return self.__date_start

    @date_start.setter
    def date_start(self, date):
        self.__date_start = date

    @property
    def date_end(self):
        return self.__date_end

    @date_end.setter
    def date_end(self, date):
        self.__date_end = date


def generate_rooms(count):
    rooms_prices = [10, 20, 100, 500, 1000]
    return [Room(i, random.choice(rooms_prices)) for i in range(1, count + 1)]
