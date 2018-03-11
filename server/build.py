"""
Builds the Django server. This involves:
    1. installing Python dependencies (`pip install -r requirements.txt`).
"""
import sys
import os

# The `server/` directory where our Django server is.
SERVER_DIR = os.path.dirname(os.path.abspath(__file__))
DEPENDENCY_FILE = 'requirements.txt'

def dependencies():
    """Install Python dependencies"""
    print('Installing Python dependencies (%s)...' % DEPENDENCY_FILE)
    os.chdir(SERVER_DIR)
    os.system('pip install -r %s' % DEPENDENCY_FILE)

def main(args):
    """Main function"""
    dependencies()

if __name__ == '__main__':
    main(sys.argv)