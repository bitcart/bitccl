class BitCCLError(Exception):
    """Base error class"""


class CompilationRestrictedError(BitCCLError):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"Those language features were restricted for your security: {self.message}"
