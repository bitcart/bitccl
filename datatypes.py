from collections import defaultdict


class ExtendedDict(defaultdict):
    def __getattribute__(self, name):
        return super().__getitem__(name)
