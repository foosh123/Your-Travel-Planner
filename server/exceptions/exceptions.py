
class DataAlreadyExistsException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class NoSuchDataException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class InvalidInputException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class InvalidJWTException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

class EmailNotSentException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
