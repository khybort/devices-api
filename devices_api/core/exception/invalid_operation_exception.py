class InvalidOperationError(BaseException):
    message: str = 'Invalid Operation on entity'

    def __init__(self, message):
        self.message = message