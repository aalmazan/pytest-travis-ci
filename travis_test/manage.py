#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import sys

if __name__ == "__main__":
    sys.path.append(os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)))
    if 'DJANGO_SETTINGS_MODULE' not in os.environ:
        raise KeyError("The environment variable 'DJANGO_SETTINGS_MODULE' must be defined")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
