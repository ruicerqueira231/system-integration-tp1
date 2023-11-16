import xml.etree.ElementTree as ET
import xml.dom.minidom as md
from csv_reader import CSVReader
from entities.country import Country
from entities.product import Product
from entities.order import Order
from entities.state import State

class CSVtoXMLConverter:
    def __init__(self, path):
        self._reader = CSVReader(path)

    def to_xml(self):
        # read countries
        countries = self._reader.read_entities(
            attr="Country",
            builder=lambda row: Country(row["Country"])
        )

        # read products
        products = self._reader.read_entities(
            attr="Product",
            builder=lambda row: Product(
                name=row["Product"],
                category=row["Product_Category"],
                sub_category=row["Sub_Category"]
            )
        )

        #read state
        def after_creating_state(state, row):
            countries[row["Country"]].add_state(state)

            state = self._reader.read_entities(
                attr = "state",
                builder=lambda row: State(
                    name=row["State"]
                ),
                after_create=after_creating_state
            )

        # read orders
        def after_creating_order(order, row):
            # add the order to the appropriate product
            products[row["Product"]].add_order(order)

        orders = self._reader.read_entities(
            attr="Order_Quantity",
            builder=lambda row: Order(
                date=row["Date"],
                customer_age=row["Customer_Age"],
                age_group=row["Age_Group"],
                customer_gender=row["Customer_Gender"],
                country=countries[row["Country"]],
                product=products[row["Product"]],
                order_quantity=row["Order_Quantity"],
                unit_cost=row["Unit_Cost"],
                unit_price=row["Unit_Price"],
                profit=row["Profit"],
                cost=row["Cost"],
                revenue=row["Revenue"]
            ),
            after_create=after_creating_order
        )

        # generate the final xml
        root_el = ET.Element("SalesData")

        products_el = ET.Element("Products")
        for product in products.values():
            products_el.append(product.to_xml())

        countries_el = ET.Element("Countries")
        for country in countries.values():
            countries_el.append(country.to_xml())

        root_el.append(products_el)
        root_el.append(countries_el)

        return root_el

    def to_xml_str(self):
        xml_str = ET.tostring(self.to_xml(), encoding='utf8', method='xml').decode()
        dom = md.parseString(xml_str)
        return dom.toprettyxml()

