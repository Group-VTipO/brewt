class InvalidEmailException(Exception):
    def __init__(self, message="Invalid email address. Debil ty zabyl vot eto @"):
        self.message = message
        super().__init__(self.message)
