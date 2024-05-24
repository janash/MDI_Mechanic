"""
Determine the Docker Compose command to use.
"""

import subprocess


import logging


def determine_compose():
    """
    Determine the compose command to use
    """

    try:
        subprocess.run(
            ["docker", "compose", "version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )
        return ["docker", "compose"]
    except (subprocess.CalledProcessError, FileNotFoundError):
        try:
            subprocess.run(
                ["docker-compose", "version"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=True,
            )
            return ["docker-compose"]
        except (subprocess.CalledProcessError, FileNotFoundError):
            logging.warning("Unable to find docker-compose or docker compose.")

COMPOSE_COMMAND = determine_compose()
