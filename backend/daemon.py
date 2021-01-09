from backend import django_setup
import logging
from backend.django_log_handler import DjangoHandler


def main():
    logger = logging.getLogger()
    logger.addHandler(DjangoHandler())
    logger.setLevel(logging.INFO)
    logger.info("log message with logger")
    logging.info("log message with logging")


if __name__ == '__main__':
    main()
