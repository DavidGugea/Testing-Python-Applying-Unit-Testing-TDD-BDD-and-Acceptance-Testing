"""This file defines and runs paver tasks for unit testing/linting/type checking/code formatting etc."""

from paver.tasks import task
from paver.easy import sh


@task
def unit_tests():
    """Run all unit tests using pytest"""
    sh('pytest --verbose')