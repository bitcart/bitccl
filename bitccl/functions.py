import secrets
import smtplib
import string
from email.message import EmailMessage

import jinja2

from .state import config as config_ctx
from .state import event_listeners
from .utils import prepare_event, silent_debug, time_limit

PASSWORD_ALPHABET = string.ascii_uppercase + string.ascii_lowercase + string.digits + "-_"
SECURE_PASSWORD_LENGTH = 43


def add_event_listener(event, func):
    event = prepare_event(event)
    event_listeners[event].append(func)


def on(event):
    def wrapper(func):
        add_event_listener(event, func)

    return wrapper


def dispatch_event(event, *args, **kwargs):
    event = prepare_event(event)
    for listener in event_listeners[event]:
        try:
            with time_limit(30):
                listener(*event.parsed_args, *args, **kwargs)
        except BaseException:
            silent_debug()
            pass


def template(name, data={}):
    try:
        with open(f"templates/{name}.j2") as f:
            template = jinja2.Template(f.read(), trim_blocks=True)
        return template.render(**data)
    except BaseException:
        silent_debug()
        return ""


def send_email(to, subject, text):  # pragma: no cover
    try:
        config = config_ctx.get()
        server = smtplib.SMTP(config.email_host, config.email_port)
        if config.email_tls:
            server.starttls()
        server.login(config.email_user, config.email_password)
        message = EmailMessage()
        message["From"] = config.email_user
        message["To"] = to
        message["Subject"] = subject
        message.set_content(text)
        server.send_message(message)
        server.quit()
        return True
    except BaseException:
        silent_debug()
        return False


def password(length=SECURE_PASSWORD_LENGTH):
    return "".join(secrets.choice(PASSWORD_ALPHABET) for _ in range(length))
