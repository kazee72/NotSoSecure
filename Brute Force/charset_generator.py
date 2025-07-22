import string
import itertools

class CharsetGenerator:

    def __init__(self, use_lower, use_upper, use_digits, use_symbols, min_length, max_length):
        self.use_lower = use_lower
        self.use_upper = use_upper
        self.use_digits = use_digits
        self.use_symbols = use_symbols
        self.min_length = min_length
        self.max_length = max_length

    def build_charset(self):
        parts = [string.ascii_lowercase if self.use_lower else "",
                 string.ascii_uppercase if self.use_upper else "",
                 string.digits if self.use_digits else "",
                 string.punctuation if self.use_symbols else ""]

        return "".join(parts)

    def generate_with_prefix(self, prefix):
        charset = self.build_charset()

        for length in range(self.min_length, self.max_length + 1):
            for suffix in itertools.product(charset, repeat=length-1):
                yield prefix + "".join(suffix)