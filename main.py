#!/bin/python

from logger.logger import configure_logging, get_logger


def main():
    print("Hej") # This is only logged to the console (avoid print)

    configure_logging(use_config="main")
    LOG = get_logger()
    LOG.info("Kalle kula")

    LOG = get_logger(logger_name="main_logger_2")
    LOG.info("Sara sahara")

    configure_logging(use_config="rotating")
    LOG = get_logger(logger_name="main_logger_1")
    LOG.info("Nisse pisse")
    LOG.error("Iiiiii, det blev ett fel!!!")
    LOG.error("Baaaah, det blev ett fel till!!!")

if __name__ == "__main__":
    main()