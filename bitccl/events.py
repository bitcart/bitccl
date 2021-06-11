class BaseEvent:

    name: str
    args_len: int = 0
    required_len: int = 0

    @classmethod
    def init_imports(cls):
        from bitccl.functions import dispatch_event

        cls._dispatch_event = dispatch_event

    def __init__(self, *args):
        args_len = len(args)
        if args_len < self.required_len:
            raise TypeError(f"Event {self.name} missing required arguments")
        if args_len > self.args_len:
            raise TypeError(f"Event {self.name}: too many arguments, expected max {self.args_len}")
        self.parsed_args = list(args)

    def __hash__(self):
        return hash((self.name, *self.parsed_args))

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __repr__(self):
        return f"{self.name} event parsed_args={self.parsed_args}"

    def dispatch(self, *args, **kwargs):
        self._dispatch_event(*args, **kwargs)


# Events

# Created events


class UserCreated(BaseEvent):
    """Fired when a new user is registered
    Optional argument: email of registered user
    """

    name = "user_created"
    args_len = 1
    required_len = 0


class NotificationCreated(BaseEvent):
    """Fired when a new notification provider is created"""

    name = "notification_created"
    args_len = 0
    required_len = args_len


class TemplateCreated(BaseEvent):
    """Fired when a new template is created"""

    name = "template_created"
    args_len = 0
    required_len = args_len


class StoreCreated(BaseEvent):
    """Fired when a new store is created"""

    name = "store_created"
    args_len = 0
    required_len = args_len


class DiscountCreated(BaseEvent):
    """Fired when a new discount is created"""

    name = "discount_created"
    args_len = 0
    required_len = args_len


class ProductCreated(BaseEvent):
    """Fired when a new product is created"""

    name = "product_created"
    args_len = 0
    required_len = args_len


class InvoiceCreated(BaseEvent):
    """Fired when a new invoice is created"""

    name = "invoice_created"
    args_len = 0
    required_len = args_len


# Sync and update events


class WalletSynchronized(BaseEvent):
    """Fired when a wallet has synchronized
    Optional argument: wallet id
    """

    name = "wallet_synchronized"
    args_len = 1
    required_len = 0


class InvoiceStatus(BaseEvent):
    """Fired when invoice status changes
    Optional argument: invoice id
    """

    name = "invoice_status"
    args_len = 1
    required_len = 0


# Events fired on checkout


class ProductBought(BaseEvent):
    """Fired when a product has been paid
    Required argument: product id
    """

    name = "product_bought"
    args_len = 1
    required_len = args_len


class InvoicePaid(BaseEvent):
    """Fired when an invoice has been paid
    Optional argument: invoice id
    """

    name = "invoice_paid"
    args_len = 1
    required_len = 0
