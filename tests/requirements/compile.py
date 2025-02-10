#!/usr/bin/env python
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

if __name__ == "__main__":
    os.chdir(Path(__file__).parent)
    os.environ["CUSTOM_COMPILE_COMMAND"] = "requirements/compile.py"
    os.environ["PIP_REQUIRE_VIRTUALENV"] = "0"
    common_args = [
        "-m",
        "piptools",
        "compile",
        "--generate-hashes",
        "--allow-unsafe",
    ] + sys.argv[1:]
    # mysqlclient requirements found on each version's "Databases" documentation page:
    # https://docs.djangoproject.com/en/3.0/ref/databases/#mysql-db-api-drivers
    subprocess.run(
        [
            "python3.9",
            *common_args,
            "-P",
            "Django>=3.2a1,<3.3",
            "-P",
            "django-cms>=3.8,<3.9",
            "-o",
            "py39-django32-cms38.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python3.9",
            *common_args,
            "-P",
            "Django>=3.2a1,<3.3",
            "-P",
            "django-cms>=3.9,<3.10",
            "-o",
            "py39-django32-cms39.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python3.9",
            *common_args,
            "-P",
            "Django>=3.2a1,<3.3",
            "-P",
            "django-cms>=3.10,<3.11",
            "-o",
            "py39-django32-cms310.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python3.10",
            *common_args,
            "-P",
            "Django>=3.2a1,<3.3",
            "-P",
            "django-cms>=3.8,<3.9",
            "-o",
            "py310-django32-cms38.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python3.10",
            *common_args,
            "-P",
            "Django>=3.2a1,<3.3",
            "-P",
            "django-cms>=3.9,<3.10",
            "-o",
            "py310-django32-cms39.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python3.10",
            *common_args,
            "-P",
            "Django>=3.2a1,<3.3",
            "-P",
            "django-cms>=3.10,<3.11",
            "-o",
            "py310-django32-cms310.txt",
        ],
        check=True,
        capture_output=True,
    )


    subprocess.run(
        [
            "python3.10",
            *common_args,
            "-P",
            "Django>=4.2a1,<5.0",
            "-P",
            "django-cms>=3.11,<4.0",
            "-o",
            "py310-django42-cms311.txt",
        ],
        check=True,
        capture_output=True,
    )
    subprocess.run(
        [
            "python3.11",
            *common_args,
            "-P",
            "Django>=4.2a1,<5.0",
            "-P",
            "django-cms>=3.11,<4.0",
            "-o",
            "py311-django42-cms311.txt",
        ],
        check=True,
        capture_output=True,
    )
