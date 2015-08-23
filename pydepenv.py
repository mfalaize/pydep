import os
import threading
import sys
import time
import subprocess

import pip


class Loading(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.terminated = False

    def run(self):
        while not self.terminated:
            print('.', end='', flush=True)
            time.sleep(1)

    def stop(self, return_code, error_message=None):
        self.terminated = True
        if return_code == 0:
            print('\033[92mDone\033[0m')
        else:
            print('\033[91mError\033[0m')
            if error_message is not None:
                print('\033[91m' + error_message + '\033[0m')


def install(dependency, version=None, error_message=None):
    app = dependency
    if version is not None:
        dependency += '==' + version
        app += '-' + version

    print('Installing {}...'.format(app), end='', flush=True)

    thread = Loading()
    thread.start()

    error = pip.main(['install', dependency, '--quiet', '--upgrade'])

    thread.stop(error, error_message)

    if error != 0:
        sys.exit(error)


def main():
    if not os.path.isfile('install_dependencies.py'):
        print('\033[91mFile install_dependencies.py cannot be found\033[0m')
        sys.exit(-1)

    print('Upgrading pip if necessary...', end='', flush=True)

    thread = Loading()
    thread.start()

    code = pip.main(['install', '--upgrade', 'pip', '--quiet'])

    thread.stop(code, 'Unable to upgrade pip')

    if code != 0:
        sys.exit(code)

    if not os.path.isfile('.env/bin/python'):
        try:
            import virtualenv
        except ImportError:
            install('virtualenv')
            import virtualenv

        print('Creating virtualenv...', end='', flush=True)

        thread = Loading()
        thread.start()

        # FIXME Should not use --system-site-packages
        sys.argv = [None, '.env', '--quiet', '--system-site-packages']
        virtualenv.main()

        # FIXME Does not work if the virtualenv creation fail because the exit code is always 0
        thread.stop(0, 'Unable to create virtualenv')

    process = subprocess.Popen(['.env/bin/python', 'install_dependencies.py'])
    code = process.wait()

    if code != 0:
        sys.exit(code)
