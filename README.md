# Py Logger

A custom logging solution for Python with additional features and color-coded output.

## Introduction

`py-logger` is a Python package that provides a powerful and customizable logging solution. It sets up logging to both a file and the console, with different log levels and formatting options. The package also includes support for custom log levels, such as "SUCCESS" and "FAILED", which are displayed in different colors to make them stand out. The Logger class uses a singleton pattern to ensure that there is only one instance of the logger throughout your application.

A log_exception decorator is also provided, which can be used to log exceptions raised by functions. The decorator logs the exception message and stack trace at the ERROR level, making it easy to track down issues in your application.

## Installation

You can install the `py-logger` package directly from the Git repository using Poetry:

```
poetry add git+https://github.com/SudarshanVK/py-logger.git
```

## Features

1. Logging to File and Console: The Logger class sets up logging to both a file and the console, with separate log levels and formatting options for each.
2. Custom Log Levels: In addition to the standard log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL), the Logger class includes two custom log levels: "SUCCESS" and "FAILED".
3. Color-Coded Output: The console log messages are color-coded based on the log level, with the "SUCCESS"messages displayed in green and the "FAILED" messages displayed in bright red.
4. Singleton Pattern: The Logger class uses a singleton pattern, ensuring that there is only one instance of the logger throughout your application.
5. Configurable Log Formats: You can customize the log formats for both the file and console handlers, as well as the time format used in the log messages.
6. Environment Variable for Console Log Level: The console log level can be set using the `CONSOLE_LOG_LEVEL` environment variable, allowing you to easily adjust the verbosity of the console output.

## Usage

To use the py-logger package in your Python application, follow these steps:

1. Import the Logger class from the my_logger module:

```python
from py_logger import logger
```
2. Create a singleton instance of the Logger class:

```python
log = logger.Logger("app.log")
```

3. Use the logging methods to log messages:

``` python
log.debug("This is a debug message.")
log.info("This is an info message.")
log.warning("This is a warning message.")
log.error("This is an error message.")
log.critical("This is a critical message.")
log.success("Operation completed successfully.")
log.failed("Something went wrong.")

# Log an exception
# divide by zero
try:
    divide_by_zero()
except Exception as e:
    log.exception(e)

```

The log messages will be written to both the app.log file and the console, with the appropriate log levels and color formatting.
Customization
You can customize the Logger class by passing additional parameters to the constructor:

1. file_format: The log format for the file handler (default: "%(asctime)s | %(name)s | %(levelname)-8s | %(funcName)s:%(lineno)d - %(message)s").
2. console_format: The log format for the console handler (default: "%(asctime)s | %(levelname)-8s | %(message)s").
3. time_format: The time format for the log messages (default: "%Y-%m-%d %H:%M:%S").

For example:

```python
from py_logger import logger

LOGGER = logger.Logger(
    "app.log",
    file_format="%(asctime)s | %(name)s | %(levelname)-8s | %(message)s",
    console_format="%(asctime)s | %(levelname)-8s | %(message)s",
)

```
This will change the log format for both the file and console handlers.

## Author

Sudarshan Vijaya Kumar