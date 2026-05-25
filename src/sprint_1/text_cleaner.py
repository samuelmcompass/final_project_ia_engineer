import re


class TextCleaner:

    def __init__(self, original_text):
        self.original_text = original_text

    def remove_extra_spaces(self):
        self.original_text = re.sub(r'\s+', ' ', self.original_text)
        return self.original_text

    def remove_special_characters(self):
        self.original_text = re.sub(
            r'[^a-zA-Z0-9\s\.,@-]',
            '',
            self.original_text
        )
        return self.original_text

    def to_lowercase(self):
        self.original_text = self.original_text.lower()
        return self.original_text

    def get_clean_text(self):
        return self.original_text