# This file mainly exists to allow python setup.py test to work.
import os, sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
test_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, test_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'test_project.settings'

from django.conf import settings
from django.test.utils import get_runner

def runtests():
    TestRunner = get_runner(settings)
    test_runner = TestRunner(verbosity=1, interactive=True)
    return test_runner.build_suite(['tester'])

if __name__ == '__main__':
    runtests()
