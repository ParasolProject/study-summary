# coding = utf-8

"""
Usage:
    docoptDemo.py [-gdtkz] <from> <to> <date>


Options:
    -h --help   Show this screen.
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达
"""
from docopt import docopt

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Naval Fate 2.0')
    print(arguments)
