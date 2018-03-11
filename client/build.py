"""
Builds the client server. This involves:
    1. Compiling LESS styles into `compiled.css`.
"""
import sys
import os

# The `server/` directory where our Django server is.
CLIENT_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_CSS_COMPILED = 'compiled.css'
SITE_LESS = 'main.less'
DEPENDENCY_FILE = 'bower.json'


def styles():
    """Compile LESS styles"""
    path = os.path.join(CLIENT_DIR, 'static')
    os.chdir(path)
    print('Compiling "%s" styles to "%s"...' % (SITE_LESS, SITE_CSS_COMPILED))
    os.system('lessc %s %s' % (SITE_LESS, SITE_CSS_COMPILED))

def main(args):
    """Main function"""
    print('Building: %s' % args)
    styles()
    print('Done.')

if __name__ == '__main__':
    main(sys.argv)

