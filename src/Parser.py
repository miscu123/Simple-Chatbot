"""
The parsing .py file to process the input and return an output
"""
from fuzzywuzzy import process
import re


class Parser:
    def __init__(self):
        pass

    def parse_txt(self, text):
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)  # remove any characters that are not numbers or letters
        text = re.sub(r'\s+', ' ', text).strip()  # normalize the space to be just one: ' '
        return text

    # fuzzywuzzy function to match the input to a specific output
    # it currently has a 20 input error margin - can be modified
    def match_fuzzy(self, user_input, options, cutoff=80):
        parsed_input = self.parse_txt(user_input)  # get the parsed text
        match, score = process.extractOne(parsed_input, options)  # match it to an output
        if score >= cutoff:
            return match  # return the match if found
        return None  # return nothing if no match found