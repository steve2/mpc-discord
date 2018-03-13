"""
Runs the application server and client modules.
"""
import argparse
import os
import sys

from threading import Thread


DEBUG_PORT = 8080 # Django debug server port.
ROOT_DIR = os.path.dirname(os.path.realpath(__file__))


def _run_command(command):
    out = os.system(command)
    print('%s [%d]' % (command, out))
    if out is not 0:  # Raise an exception if the command fails.
        raise Exception('Command failed: %s' % command)


def _run_server(port=DEBUG_PORT):
    if os.name == 'nt':
        python_path = os.path.join(ROOT_DIR, 'server', 'env', 'Scripts', 'python.exe')
    else:
        python_path = os.path.join(ROOT_DIR, 'server', 'env', 'bin', 'python')
    manage_path = os.path.join(ROOT_DIR, 'server', 'manage.py')
    _run_command('%s %s runserver %s' % (python_path, manage_path, port))


def _build_client():
    _run_command('python %s' % os.path.join(ROOT_DIR, 'client', 'build.py'))


def _main(args):
    parser = argparse.ArgumentParser(description='Run the project.')
    parser.add_argument('--server-port', action='store')
    args = parser.parse_args()

    _build_client()

    port_override = args.server_port if args.server_port is not None else DEBUG_PORT
    server_thread = Thread(target=_run_server, args=(int(port_override),))
    server_thread.start()


if __name__ == '__main__':
    _main(sys.argv)
