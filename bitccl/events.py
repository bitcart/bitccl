class BaseEvent:

    name: str
    args_len: int = 0
    required_len: int = 0

    @classmethod
    def init_imports(cls):
        from .functions import dispatch_event

        cls._dispatch_event = dispatch_event

    def __init__(self, *args):
        args_len = len(args)
        if args_len < self.required_len:
            raise TypeError(f"Event {self.name} missing required arguments")
        if args_len > self.args_len:
            raise TypeError(
                f"Event {self.name}: too many arguments, expected max {self.args_len}"
            )
        self.parsed_args = list(args)

    def __hash__(self):
        return hash((self.name, *self.parsed_args))

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __repr__(self):
        return f"{self.name} event parsed_args={self.parsed_args}"

    def dispatch(self, *args, **kwargs):
        self._dispatch_event(*args, **kwargs)


class ProductBought(BaseEvent):
    name = "product_bought"
    args_len = 1
    required_len = args_len
