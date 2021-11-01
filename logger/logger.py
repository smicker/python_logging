import logging
import logging.config
from os import getcwd


def configure_logging(use_config: str = "main") -> None:
    """Configure log framework"""
    if use_config == "main":
        logging.config.fileConfig(
            # Path to the configuration file
            fname=getcwd() + "/logger/main_log.conf",
            # If set to true (default) all previously defined
            # loggers are disabled, including default loggers.
            # This is probably never what you want.
            disable_existing_loggers=False,
            # Below passes the current work dir as the variable
            # "logfilepath" into the main_log.conf file. That
            # makes it possible to set the path for the output
            # log file.
            defaults={"logfilepath": getcwd()},
        )
    else:
        logging.config.fileConfig(
            fname=getcwd() + "/logger/rotating_log.conf",
            disable_existing_loggers=False,
            defaults={"logfilepath": getcwd()},
        )


def get_logger(logger_name="main_logger_1") -> logging.Logger:
    return logging.getLogger(logger_name)

