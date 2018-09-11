
import logging
import logging.handlers
import functools

def log_init():
    logger = logging.getLogger("test_log")
    logger.setLevel(logging.DEBUG)

    fn = logging.handlers.TimedRotatingFileHandler('log.log', when='midnight')

    fn.setLevel(logging.DEBUG)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(message)s")

    fn.setFormatter(formatter)

    logger.addHandler(fn)

    return logger

logger = log_init()

def log(logger):
    def deco(func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
        return wrapper
    return deco

@log(logger)
def conn_info(addr):
    logger.info("CONNECTED:" + str(addr))

@log(logger)
def disconn_info(addr):
    logger.info("DISCONNECTED:" + str(addr))

@log(logger)
def conn_exception(e):
    logger.warn(str(e))
