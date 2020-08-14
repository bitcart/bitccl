import logging


def init_logger(name, testing_mode) -> logging.Logger:
    log_format = "%(asctime)s - " "%(name)s - " "%(funcName)s - " "%(levelname)s - " "%(message)s"
    logging.basicConfig(format=log_format)
    logger = logging.getLogger(name)

    if testing_mode:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    return logger


logger = init_logger(__name__, testing_mode=False)
