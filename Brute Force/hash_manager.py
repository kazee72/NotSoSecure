import hashlib

class HashManager:

    def __init__(self, hash_algorithm):
        self.hash_algorithm = hash_algorithm.lower()

    def hash(self, input):
        byte_input = input.encode() # encode input to bytes

        # make hasher obj based on hash_algorithm
        match self.hash_algorithm:
            case "sha256":
                hasher = hashlib.sha256()

            case "sha1":
                hasher = hashlib.sha1()

            case "md5":
                hasher = hashlib.md5()

            case _:
                raise ValueError

        hasher.update(byte_input) # feed the bytes into hasher
        hex_string = hasher.hexdigest() # get hex string

        return hex_string

    def is_match(self, guess, target_hash):
        return self.hash(guess) == target_hash
