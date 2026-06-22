#!/usr/bin/env python
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

# django-cms 5.1's migrations are incompatible with django-treebeard >= 5
# (changed numconv signature), so pin treebeard below 5 for those environments.
CMS51_PINS = ["django-treebeard<5"]

# (python interpreter, Django spec, django-cms spec, extra pins, output file)
# django-cms 5.1 is still a pre-release, so the spec allows pre-releases.
MATRIX = [
    ("python3.12", "Django>=5.2,<6.0", "django-cms>=5.0,<5.1", [], "py312-django52-cms50.txt"),
    ("python3.12", "Django>=5.2,<6.0", "django-cms>=5.1a1,<5.2", CMS51_PINS, "py312-django52-cms51.txt"),
    ("python3.12", "Django>=6.0,<6.1", "django-cms>=5.0,<5.1", [], "py312-django60-cms50.txt"),
    ("python3.12", "Django>=6.0,<6.1", "django-cms>=5.1a1,<5.2", CMS51_PINS, "py312-django60-cms51.txt"),
    ("python3.13", "Django>=5.2,<6.0", "django-cms>=5.0,<5.1", [], "py313-django52-cms50.txt"),
    ("python3.13", "Django>=5.2,<6.0", "django-cms>=5.1a1,<5.2", CMS51_PINS, "py313-django52-cms51.txt"),
    ("python3.13", "Django>=6.0,<6.1", "django-cms>=5.0,<5.1", [], "py313-django60-cms50.txt"),
    ("python3.13", "Django>=6.0,<6.1", "django-cms>=5.1a1,<5.2", CMS51_PINS, "py313-django60-cms51.txt"),
    ("python3.14", "Django>=5.2,<6.0", "django-cms>=5.0,<5.1", [], "py314-django52-cms50.txt"),
    ("python3.14", "Django>=5.2,<6.0", "django-cms>=5.1a1,<5.2", CMS51_PINS, "py314-django52-cms51.txt"),
    ("python3.14", "Django>=6.0,<6.1", "django-cms>=5.0,<5.1", [], "py314-django60-cms50.txt"),
    ("python3.14", "Django>=6.0,<6.1", "django-cms>=5.1a1,<5.2", CMS51_PINS, "py314-django60-cms51.txt"),
]

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
    for interpreter, django_spec, cms_spec, extra_pins, output in MATRIX:
        pins = []
        for spec in (django_spec, cms_spec, *extra_pins):
            pins += ["-P", spec]
        subprocess.run(
            [
                interpreter,
                *common_args,
                *pins,
                "-o",
                output,
            ],
            check=True,
            capture_output=True,
        )
