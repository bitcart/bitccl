from collections import defaultdict

from bitccl.datatypes import ExtendedDict
from bitccl.utils import load_config


class ConfigSingleton:
    data = load_config()

    @classmethod
    def set(cls, config):
        cls.data = ExtendedDict(lambda: None, **config)

    @classmethod
    def get(cls):
        return cls.data


event_listeners = defaultdict(list)
config = ConfigSingleton
