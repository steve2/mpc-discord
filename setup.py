"""
Runs the application server and client modules.
    Requirements:
        - python34
        - virtualenv (pip install virtualenv)
        - npm
"""

from threading import Thread
from argparse import RawTextHelpFormatter
import argparse
import os


# The directory of this file should be the root directory of the project.
ROOT_DIR = os.path.dirname(os.path.realpath(__file__))

# Path to virtualenv binaries for setup.
if os.name == 'nt':
    PYTHON = os.path.join(ROOT_DIR, 'server', 'env', 'Scripts', 'python.exe')
    PIP = os.path.join(ROOT_DIR, 'server', 'env', 'Scripts', 'pip.exe')
else:
    PYTHON = os.path.join(ROOT_DIR, 'server', 'env', 'bin', 'python')
    PIP = os.path.join(ROOT_DIR, 'server', 'env', 'bin', 'pip')

####################################################################
#
#   HELPER FUNCTIONS
#
####################################################################

def _set_directory(subdir):
    """Sets the current working directory for system commands."""
    working_dir = os.path.join(ROOT_DIR, subdir)
    os.chdir(working_dir)
    print('Current directory: %s' % working_dir)


def _run_command(command):
    """Runs a system command. Raises an exception if the command fails."""
    out = os.system(command)
    print('%s [%d]' % (command, out))
    if out is not 0:  # Raise an exception if the command fails.
        raise Exception('Command failed: %s' % command)


def _print_setup_error(error):
    """Displays the error that occurred during initialization."""
    print('Setup failed due to:\n\t%s' % str(exception))


####################################################################
#
#   PROGRAM ENTRY POINT
#
####################################################################

def __main__():
    
    description = 'Setup development environment.\n\n' \
        'If you have already run this script, it may be necessary to \n' \
        'skip virtual environment and superuser setup. This can be \n' \
        'done with options `--skip-venv` and `--skip-superuser`.\n\n' \
        'If you need to use a different version of Python for your \n' \
        'virtual environment, use the `--venv-python` argument. It \n' \
        'may be necessary to specify Python 3 if both versions are \n' \
        'installed. This doesn\'t apply if `--skip-venv` is specified.'

    parser = argparse.ArgumentParser(description=description, formatter_class=RawTextHelpFormatter)
    parser.add_argument('--skip-venv', action='store_true', help='skip virtual environment setup')
    parser.add_argument('--skip-pip', action='store_true', help='skip pip upgrade')
    parser.add_argument('--skip-migrate', action='store_true', help='skip Django migration')
    parser.add_argument('--skip-superuser', action='store_true', help='skip Django superuser creation')
    parser.add_argument('--skip-server', action='store_true', help='skips the entire server setup')
    parser.add_argument('--skip-client', action='store_true', help='skips client bower/npm setup')
    parser.add_argument('--venv-python', action='store', help='python to use with virtual environment (for server)')
    args = parser.parse_args()

    try:
        
        ############################################################
        #
        #   SERVER SETUP
        #
        ############################################################

        if not args.skip_server:
            _set_directory('server')

            # ------------------------------------------------------
            # Initialize virtual environment.

            if not args.skip_venv:
                if args.venv_python:
                    _run_command('virtualenv --python=%s env' % args.venv_python)
                else:
                    _run_command('virtualenv env')
            else:
                print('Skipping virtual environment setup.')

            # ------------------------------------------------------
            # Update pip to latest version.

            if not args.skip_pip:
                _run_command('%s -m pip install --upgrade pip' % PYTHON)
            else:
                print('Skipping pip update.')

            # ------------------------------------------------------
            # Install Python dependencies.

            _run_command('%s install -r requirements.txt' % PIP)

            # ------------------------------------------------------
            # Django migrations.
            
            if not args.skip_migrate:
                _run_command('%s manage.py migrate' % PYTHON)
            else:
                print('Skipping Django migrations.')

            # ------------------------------------------------------
            # Create Django superuser.

            if not args.skip_superuser:
                _run_command('%s manage.py createsuperuser' % PYTHON)
            else:
                print('Skipping Django Admin superuser creation.')
        else:
            print('Skipping server setup.')

        
        ############################################################
        #
        #   CLIENT SETUP
        #
        ############################################################

        if not args.skip_client:
            
            # Can't seem to install BOWER and LESS this way.
            # On Ubuntu, this leaves a broken installation.
            # npm_install = 'npm install'
            # if os.name != 'nt':
            #     npm_install = 'sudo ' + npm_install
            # _run_command('%s -g bower' % npm_install)
            # _run_command('%s -g less' % npm_install)
            
            # ------------------------------------------------------
            # Install NPM packages.
            
            if os.path.exists(os.path.join('client', 'package.json')):
                _set_directory('client')
                _run_command('npm install')
            else:
                print('Skipping `npm install` because there was no `package.json` file.')
            
            # ------------------------------------------------------
            # Install Bower components.

            if os.path.exists(os.path.join('client', 'static', 'bower.json')):
                _set_directory(os.path.join('client', 'static'))
                _run_command('bower install')
            else:
                print('Skipping `bower install` because there was no `bower.json` file.')
        else:
            print('Skipping client setup.')

    except Exception as exception:
        _print_setup_error(exception)

