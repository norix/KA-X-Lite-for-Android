#!/usr/bin/env python
import os, sys

PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))

sys.path = [PROJECT_PATH, os.path.join(PROJECT_PATH, "../"), os.path.join(PROJECT_PATH, "../python-packages/")] + sys.path

from django.core.management import execute_manager
import settings

if __name__ == "__main__":
    execute_manager(settings)
