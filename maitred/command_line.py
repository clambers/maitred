from argparse import ArgumentParser
from configparser import ConfigParser
from inspect import getdoc
from klein import run, route


@route('/')
def home(request):
    print('got a notification')


def main():
    """Run a small web server that listens for GitLab notifications and
    routes them to their appropriate receivers.

    """
    ap = ArgumentParser(description=getdoc(main))
    parsed = ap.parse_args()

    if parsed is None:
        return

    cp = ConfigParser()
    cp.read(['/etc/maitred.conf'])

    run('localhost', 8080)
