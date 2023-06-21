class UserException(Exception):
    pass


class WrongEmailException(UserException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class WrongPasswordException(UserException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
