import os
import logging

from enum import Enum


def get_env_variable(var_name, default=None):
    try:
        return os.environ[var_name]
    except KeyError:
        if default is not None:
            return default
        error_msg = "Set the {} environment variable".format(var_name)
        logging.error(error_msg)


class EnvironmentVariables(Enum):
    DB_HOST = 'DB_HOST'
    DB_PORT = 'DB_PORT'
    DB_USER = 'DB_USER'
    DB_PASSWORD = 'DB_PASSWORD'
    DB_NAME = 'DB_NAME'
