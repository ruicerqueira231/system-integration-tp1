import xml.etree.ElementTree as ET

class Product:
    def __init__(self, name, category, sub_category):
        Product.counter += 1
        self._id = Product.counter
        self._name = name
        self._category = category
        self._sub_category = sub_category
        self._orders = []

    def add_order(self, order):
        self._orders.append(order)

    def get_id(self):
        return self._id

    def get_orders(self):
        return self._orders

    def to_xml(self):
        el = ET.Element("Product")
        el.set("id", str(self._id))
        el.set("name", self._name)
        el.set("category", self._category)
        el.set("sub_category", self._sub_category)

        orders_el = ET.Element("Orders")
        for order in self._orders:
            orders_el.append(order.to_xml())

        el.append(orders_el)

        return el

    def __str__(self):
        return f"name: {self._name}, id:{self._id}"

Product.counter = 0

