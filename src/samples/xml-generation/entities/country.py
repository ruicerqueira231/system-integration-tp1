import xml.etree.ElementTree as ET

from entities.state import State

class Country:
    def __init__(self, name):
        Country.counter += 1
        self._id = Country.counter
        self._name = name
        self._states = []

    def to_xml(self):
        el = ET.Element("Country")
        el.set("id", str(self._id))
        el.set("name", self._name)
        state_el = ET.Element("States")
        
        for state in self._states:
            state_el.append(state.to_xml())

        el.append(state_el)

        return el
    
    def add_state(self, state: State):
        return self._states.append(state)

    def get_id(self):
        return self._id

    def __str__(self):
        return f"name= {self._name}, id= {self._id}"

Country.counter = 0



