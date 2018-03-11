"""
Builds the client project. This currently involves:
    - Compiling LESS styles into single CSS file.
"""
import os


# The root directory of the client (directory of this file).
CLIENT_DIR = os.path.dirname(os.path.realpath(__file__))

STYLE_DIR = os.path.join(CLIENT_DIR, 'static')
SITE_LESS = 'main.less' # The source style.
SITE_CSS_COMPILED = 'compiled.css' # The compiled CSS.


def _set_directory(subdir):
    """Set the current working directory"""
    working_dir = os.path.join(CLIENT_DIR, subdir)
    os.chdir(working_dir)
    print('Current directory: %s' % working_dir)


def _run_command(command):
    """Run a system command and print the output"""
    out = os.system(command)
    print('%s [%d]' % (command, out))
    if out is not 0: # Raise an exception if the command fails.
        raise Exception('Command failed: %s' % command)


def compile_less():
    """Compile LESS styles into single CSS file"""
    _set_directory(STYLE_DIR)
    _run_command('lessc %s %s' % (SITE_LESS, SITE_CSS_COMPILED))


if __name__ == '__main__':
    try:
        compile_less()
    except excp:
        print(excp)
