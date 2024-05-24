"""
Determine the Docker Compose command to use.
"""

import subprocess

import os


def determine_compose(testing=False):
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
            if testing:
                return ["docker-compose"]
            else:
                # raise exception
                raise Exception(
                    "Unable to find docker-compose or docker compose."
                )

if os.getenv("TESTING") == "true":
    COMPOSE_COMMAND = determine_compose(testing=True)
else:
    COMPOSE_COMMAND = determine_compose()
