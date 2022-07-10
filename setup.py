import sys
import subprocess


with open('requirements.txt') as f:
    for package in f.read().splitlines():
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])