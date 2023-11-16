import xml.etree.ElementTree as ET

class State:

    def __init__(self, name):
        State.counter += 1
        self._id = State.counter
        self._name = name
    
    def to_xml(self):
        el = ET.Element("State")
        el.set("id", self._id)
        el.set("nome", self._name)

        return el
    
    def get_id(self):
        return self._id
    
    def __str__(self):
        return f"id={self._id}, name={self._name}"

State.counter = 0