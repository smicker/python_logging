#!/bin/python

from logger.logger import log, configure_logging


def main():
    print("Hej") # This is only logged to the console (avoid print)

    configure_logging(use_config="main")
    log("Kalle kula")
    log("Sara sahara", logger_name="main_logger_2")

    configure_logging(use_config="other")
    log("Nisse pisse")

if __name__ == "__main__":
    main()