import httpx

from bitccl.version import VERSION


def startup():
    http_client = httpx.Client(http2=True, headers={"user-agent": f"bitccl/{VERSION}"})
    return {"http": http_client, "http_codes": httpx.codes}


def shutdown(context):
    context["http"].close()
