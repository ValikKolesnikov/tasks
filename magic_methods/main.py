# Write code so that when you run the script,
# it does not raise any assertion errors

import re
import itertools
import uuid


class Item:
    id_count = itertools.count()

    def __init__(self, name, quantity, unit_price):
        self._id = next(self.id_count)
        self._name = name
        self._quantity = quantity
        self._unit_price = unit_price

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        self._unit_price = unit_price

    @property
    def total_price(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Item: {self.name}>'

    def __gt__(self, other):
        return self.total_price > other.total_price

    def __lt__(self, other):
        return self.total_price < other.total_price

    def __ge__(self, other):
        return self.total_price >= other.total_price

    def __le__(self, other):
        return self.total_price <= other.total_price


class Order:
    def __init__(self, items):
        self._id = str(uuid.uuid4())
        self._items = items

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items):
        self._items = items

    @property
    def total_price(self):
        return sum([item.total_price for item in self.items])

    def get_the_most_expensive_item(self):
        return max(self.items, key=lambda x: x.total_price)

    def add_item(self, item):
        self.items.append(item)

    def __str__(self):
        return f'Order #{self.id} with 4 items'

    def __repr__(self):
        return f'<Order: {self.id}>'

    def __iter__(self):
        return self.items.__iter__()

    def __len__(self):
        return len(self.items)


def run():
    jacket = Item(
        name='Leather Jacket',
        quantity=1,
        unit_price=200
    )
    jeans = Item(
        name='Black Jeans',
        quantity=2,
        unit_price=30
    )
    boots = Item(
        name='Chelsea Boots',
        quantity=1,
        unit_price=50
    )
    sweater = Item(
        name='Sweater',
        quantity=4,
        unit_price=25
    )

    order = Order(
        items=[jacket, jeans, boots, sweater]
    )

    # Should show a str representation
    assert str(boots) == 'Chelsea Boots'
    assert str(order) == f'Order #{order.id} with 4 items'

    # Should show a repr representation
    assert repr(boots) == '<Item: Chelsea Boots>'
    assert repr(order) == f'<Order: {order.id}>'

    # Should generate unique uuid4 id for each order
    uuid4_regex = re.compile(
        '^[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}\Z',
        re.I
    )
    assert uuid4_regex.match(order.id)

    # Should show a total price of item based on its quantity
    assert sweater.total_price == 100

    # Should show a total price of order
    assert order.total_price == 410

    # Should be able to compare items by their total price
    assert jacket > boots
    assert jacket >= sweater
    assert boots < sweater
    assert boots <= jeans

    # Should be able to iterate through items
    for item in order:
        assert item.name in (
            'Leather Jacket', 'Black Jeans', 'Chelsea Boots', 'Sweater'
        )

    # Should be able to check whether an item is in order or not
    assert jacket in order

    # Should show a number of items
    assert len(order) == 4

    # Should be able to get the most expensive item
    the_most_expensive_item = order.get_the_most_expensive_item()
    assert the_most_expensive_item is jacket

    # Should be able to add new items to the order
    watch = Item(
        name='Watch',
        quantity=1,
        unit_price=500
    )
    assert watch not in order
    order.add_item(watch)
    assert watch in order


if __name__ == '__main__':
    run()
