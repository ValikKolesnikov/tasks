import random


class Hotel:
    def __init__(self, name, rooms=[]):
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
        room.tenant = None
        print(f'Room #{room.number} is free')

    def show_price_list(self):
        for room in self.rooms:
            print(f'Room #{room.number}\n'
                  f'Is booked: {room.is_booked}\n'
                  f'Cost: ${room.cost}/day\n')

    def get_room_by_number(self, number):
        for room in self.rooms:
            if room.number == number:
                return room
        return None

    def allocate_room(self, person, room, days_count):
        if not room.tenant and days_count * person.money:
            room.tenant = person
            person.money -= days_count * room.cost
            print('Congratulations! Room is booked')
        else:
            print('You can not book this room(')


class Room:
    def __init__(self, number, cost):
        self.__number = number
        self.__cost = cost
        self.__tenant = None

    def is_booked(self):
        return not self.tenant is None

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


class Person:
    def __init__(self, name, money=100):
        self.__name = name
        self.__money = money

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, sum):
        self.__money += sum

    @property
    def name(self):
        return self.__name


def generate_rooms(count):
    rooms_prices = [10, 20, 100, 500, 1000]
    return [Room(i, random.choice(rooms_prices)) for i in range(1, count + 1)]
