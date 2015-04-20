import os
import sys


def main():
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "kinderstadt.settings.development")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
