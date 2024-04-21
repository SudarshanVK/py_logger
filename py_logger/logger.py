import inspect
import json
import logging
import os
from datetime import datetime

from rich import print
from rich.console import Console

console = Console()


class Logger:
    """
    The Logger class in Python that sets up logging to a file and console with
    different log levels and formatting options.

    :param log_file_path: The path to the log file.
    :param file_format: The log format for the file handler (default: "%(asctime)s | %(name)s | %(levelname)-8s | %(funcName)s:%(lineno)d - %(message)s").
    :param console_format: The log format for the console handler (default: "%(asctime)s | %(levelname)-8s | %(message)s").
    :param time_format: The time format for the log messages (default: "%Y-%m-%d %H:%M:%S").
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.__init__(*args, **kwargs)
        return cls._instance

    def get_timestamp(self):
        return datetime.now().strftime("%d-%m-%y %H:%M:%S")

    def get_caller_function(self):
        caller_frame = inspect.stack()[2]
        caller_function = caller_frame.function
        caller_filename = os.path.join(
            os.path.basename(os.path.dirname(caller_frame.filename)),
            os.path.basename(caller_frame.filename),
        )
        return f"{caller_filename}::{caller_function}"

    def __init__(self, log_file_path):
        if not hasattr(self, "logger"):
            self.logger = logging.getLogger()
            self.logger.setLevel(logging.DEBUG)

            # Create file handler and set level to DEBUG
            fh = logging.FileHandler(log_file_path, mode="w")
            fh.setLevel(logging.DEBUG)

            # Create stream handler and set level from environment variable
            console_log_level = os.getenv("CONSOLE_LOG_LEVEL", "INFO")
            console_log_level = getattr(
                logging, console_log_level.upper(), logging.INFO
            )
            sh = logging.StreamHandler()
            sh.setLevel(console_log_level)

            file_format = "%(asctime)s | %(levelname)-8s | %(message)s"
            console_format = "%(asctime)s | %(levelname)-8s | %(message)s"
            # Create formatters and add them to the handlers
            file_formatter = logging.Formatter(file_format, datefmt="%d-%m-%y %H:%M:%S")
            fh.setFormatter(file_formatter)

            # Add color and styling to stream handler
            class ColorFormatter(logging.Formatter):
                def format(self, record):
                    if record.levelno == logging.DEBUG:
                        color_code = "\033[34m"  # CYAN
                    elif record.levelno == logging.INFO:
                        color_code = "\033[36m"  # WHITE
                    elif record.levelno == logging.WARNING:
                        color_code = "\033[33m"  # YELLOW
                    elif record.levelno == logging.ERROR:
                        color_code = "\033[31m"  # RED
                    elif record.levelname == "FAILED":
                        color_code = "\033[91m"  # BRIGHT RED
                    elif record.levelname == "SUCCESS":
                        color_code = "\033[92m"  # BRIGHT GREEN
                    else:
                        color_code = "\033[35m"  # MAGENTA (for CRITICAL)
                    message = super().format(record)
                    return f"{color_code}{message}\033[0m"  # RESET

            console_formatter = ColorFormatter(
                console_format, datefmt="%d-%m-%y %H:%M:%S"
            )
            sh.setFormatter(console_formatter)

            # Add the handlers to the logger
            self.logger.addHandler(fh)
            self.logger.addHandler(sh)

    def add_custom_level(self, level_name, level_value):
        logging.addLevelName(level_value, level_name)
        setattr(self, level_name, lambda message: self.logger.log(level_value, message))

    def debug(self, msg, data=None):
        if data and isinstance(data, (dict, list)):
            msg += f" -\n{json.dumps(data, indent=4)}"
        self.logger.debug(msg)

    def info(self, msg, data=None):
        if data and isinstance(data, (dict, list)):
            msg += f" -\n{json.dumps(data, indent=4)}"
        self.logger.info(msg)

    def warning(self, msg, data=None):
        if data and isinstance(data, (dict, list)):
            msg += f" -\n{json.dumps(data, indent=4)}"
        self.logger.warning(f"{self.get_caller_function()} | {msg}")

    def error(self, msg, data=None):
        if data and isinstance(data, (dict, list)):
            msg += f" -\n{json.dumps(data, indent=4)}"
        self.logger.error(f"{self.get_caller_function()} | {msg}")

    def critical(self, msg, data=None):
        if data and isinstance(data, (dict, list)):
            msg += f" -\n{json.dumps(data, indent=4)}"
        self.logger.critical(f"{self.get_caller_function()} | {msg}")

    def success(self, msg, data=None):
        if data and isinstance(data, (dict, list)):
            msg += f" -\n{json.dumps(data, indent=4)}"
        print(f"{self.get_timestamp()} | [green]SUCCESS  | {msg}")

    def failed(self, msg, data=None):
        if data and isinstance(data, (dict, list)):
            msg += f" -\n{json.dumps(data, indent=4)}"
        print(f"{self.get_timestamp()} | [bold red]FAILED   | {msg}")

    def message(self, msg, data=None):
        if data and isinstance(data, (dict, list)):
            msg += f" -\n{json.dumps(data, indent=4)}"
        print(f"{self.get_timestamp()} | [cyan1]MESSAGE  | {msg}")

    def exception(self):
        console.print_exception(show_locals=True)
