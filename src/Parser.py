"""
Parser .py file to parse the message and return an answer

ex: "Ce MAI faci?" --> "ce mai faci"   |
    "CE MAI FACI" --> "ce mai faci"    | same answer for all 3 inputs
    "<><CE MAI.. faci???" --> "ce mai faci" |
"""
import re


class Parser:
    def __init__(self):
        pass

    # parse the input and remove all chars except numbers, letters and spaces
    # also normalize word spacing
    def parse_txt(self, text):
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text