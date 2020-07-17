from collections import defaultdict

from .utils import load_config

event_listeners = defaultdict(list)
config = load_config()
