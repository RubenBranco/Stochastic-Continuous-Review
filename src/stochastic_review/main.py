import logging
import argparse

from .cli import cli, get_args_from_cli
from .model import continuous_review


def _handle_command_line():
    parser = argparse.ArgumentParser(description="Stochastic Continuous Review Model")
    parser.add_argument(
        "-verbosity",
        "--v",
        dest='verbosity',
        choices=range(1,3),
        type=int,
        default=2,
        help="Verbosity of the output during the run, 1 for info only, 2 for debug.",
    )
    return parser.parse_args()


def _get_logger(level):
    LOGGER_LEVELS = {
        1:logging.INFO,
        2:logging.DEBUG,
    }

    logger = logging.getLogger('stochastic_review')
    logger.setLevel(LOGGER_LEVELS[level])
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s')
    ch = logging.StreamHandler()
    ch.setLevel(LOGGER_LEVELS[level])
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    return logger


def main():
    cl_args = _handle_command_line()
    args = get_args_from_cli(cli)
    logger = _get_logger(cl_args.verbosity)
    k, q, r, qos = continuous_review(args, logger)
    logger.info(f"Value of K*: {round(k, 2)}")
    logger.info(f"Value of Q*: {round(q, 2)}")
    logger.info(f"Value of r*: {round(r, 2)}")
    logger.info(f"Value of Quality of Service: {round(qos, 2)}")
    return k, q, r, qos
