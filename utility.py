"""Shared helpers for Advent of Code solutions.

Import this module from a day's script and use the helpers to avoid repeating
the logging, input-loading and timing boilerplate.
"""


import logging
import os
import time
import tracemalloc


logging.basicConfig(format='%(asctime)s.%(msecs)03d:%(levelname)s:%(name)s:\t%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

_logger = logging.getLogger(__name__)
_logger.setLevel(logging.INFO)


def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Return a logger configured with the shared format.

    Args:
        name: Logger name, usually the caller's ``__name__``.
        level: Logging level to set on the logger.

    Returns:
        The configured logger.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)
    return logger


def input_path(script_file: str) -> str:
    """Build the input file path for a day's script.

    Mirrors the convention ``input/<day_number>.txt`` next to the script,
    where the day number is the first two characters of the script's name.

    Args:
        script_file: The calling script's ``__file__``.

    Returns:
        Absolute path to the day's input file.
    """
    script_dir = os.path.dirname(script_file)
    day = os.path.basename(script_file).split('.')[0][:2]
    return os.path.join(script_dir, 'input', f'{day}.txt')


def monitor_execution(func) -> None:
    """Run ``func`` while logging its execution time and peak memory usage."""
    tracemalloc.start()
    t1 = time.perf_counter()
    func()
    t2 = time.perf_counter()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    _logger.info('Execution time: %0.4f seconds', t2 - t1)
    _logger.info('Peak memory usage: %0.2f KB', peak / 1024)
