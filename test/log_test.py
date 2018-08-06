# autor : colson (Yeong Jun Kim)
# https://www.github.com/YeongJunKim

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)

logger = logging.getLogger('NAME')

def set_logger_level(level):
    logger.setLevel(level)


if __name__ == '__main__':
    logger.debug("this is debug")
    logger.info("this is info")
    logger.warning("this is warning")
    logger.error("this is error")
    logger.critical("this is critical")

    set_logger_level(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    logger.propagate = 0

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    file_handler = logging.FileHandler('logger.log')
    logger.addHandler(file_handler)
    logger.info("server start!!")









