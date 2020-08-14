import httpx

from ..utils import mark_allowed_imports
from ..version import VERSION


def startup():
    http_client = mark_allowed_imports(httpx.Client(http2=True, headers={"user-agent": f"bitccl/{VERSION}"}))
    return {"http": http_client, "http_codes": httpx.codes}


def shutdown(context):
    context["http"].close()
