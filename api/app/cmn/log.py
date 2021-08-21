import logging


def get_logger(modname: str, is_debug=False) -> logging.Logger:
    logger = logging.getLogger(modname)
    handler = logging.StreamHandler()
    logger.addHandler(handler)
    is_debug and logger.setLevel(logging.DEBUG)
    return logger
