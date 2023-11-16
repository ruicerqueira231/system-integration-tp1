import xml.etree.ElementTree as ET

class Order:
    def __init__(self, date, customer_age, age_group, customer_gender, country, product,
                 order_quantity, unit_cost, unit_price, profit, cost, revenue):
        self._date = date
        self._customer_age = customer_age
        self._age_group = age_group
        self._customer_gender = customer_gender
        self._country = country
        self._product = product
        self._order_quantity = order_quantity
        self._unit_cost = unit_cost
        self._unit_price = unit_price
        self._profit = profit
        self._cost = cost
        self._revenue = revenue

    def to_xml(self):
        el = ET.Element("Order")
        el.set("date", str(self._date))
        el.set("customer_age", str(self._customer_age))
        el.set("age_group", str(self._age_group))
        el.set("customer_gender", str(self._customer_gender))
        el.set("country_ref", str(self._country.get_id()))
        el.set("order_quantity", str(self._order_quantity))
        el.set("unit_cost", str(self._unit_cost))
        el.set("unit_price", str(self._unit_price))
        el.set("profit", str(self._profit))
        el.set("cost", str(self._cost))
        el.set("revenue", str(self._revenue))

        return el
