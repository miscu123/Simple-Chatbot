from fuzzywuzzy import process
import re


class Parser:
    def __init__(self):
        pass

    def parse_txt(self, text):
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    def match_fuzzy(self, user_input, options, cutoff=70):
        parsed_input = self.parse_txt(user_input)
        match, score = process.extractOne(parsed_input, options)
        if score >= cutoff:
            return match
        return None