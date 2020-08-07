from bitccl import events
from bitccl.events import BaseEvent

out = "events.md"

f = open(out, "w")
for event in events.values():
    if event != BaseEvent:
        print(f"`{event.__name__}`\n\n{event.__doc__}\n".replace("    ", "\n"), file=f)

f.close()
