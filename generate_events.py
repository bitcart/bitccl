from bitccl.compiler import events
from bitccl.events import BaseEvent

output = ""
SPACES = " " * 4

for event in events.values():
    if event != BaseEvent:
        output += f"`{event.__name__}`\n\n{event.__doc__.strip()}\n\n".replace(SPACES, "\n")

with open("events.md", "w") as f:
    print(output.strip(), file=f)
