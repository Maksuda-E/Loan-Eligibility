#  defines a custom project exception class.
class ProjectException(Exception):
    #  initializes the custom exception.
    def __init__(self, message: str):
        #  calls the parent exception constructor.
        super().__init__(message)

        #  stores the exception message.
        self.message = message