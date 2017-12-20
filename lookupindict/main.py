#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from optparse import OptionParser

from . import lookup
from . import __version__


def _parse_options():
    """Parses md2slides's command line options"""

    parser = OptionParser(
        usage="%prog [options] word/phrase",
        description="look up a word or a phrase in dict.cn and save it",
        epilog="Note: a phrase should be written as 'look_up'",
        version="%prog " + __version__)

    parser.add_option(
            "-s", "--save",
            action="store_true",
            dest="save",
            help="save this word/phrase ?",
            default=False)

    parser.add_option(
        "-l", "--localpath",
        dest="output_dir",
        help="local path to the dir saving the words",
        metavar="DIR",
        default='dir_lookupindict')


    (options, args) = parser.parse_args()

    if not args:
        parser.print_help()
        sys.exit(1)

    return options, args[0]


def log(message, type):
    """Log notices to stdout and errors to stderr"""

    (sys.stdout if type == 'notice' else sys.stderr).write(message + "\n")


def run(word, options):
    """Runs the Converter using parsed options."""

    options.logger = log
    lookup.Lookup(word, **options.__dict__).execute()

def show_info():

    print '########################################'
    print '######   lookupindic             #######'
    print '######    Look up a word/phrase  #######'
    print '######     from dict.cn          #######'
    print '######      Make my life easy!   #######'
    print '########################################'

def main():
    """Main program entry point"""

    show_info()

    options, word = _parse_options()

    try:
        run(word, options)
    except Exception as e:
        sys.stderr.write("Error: %s\n" % e)
        sys.exit(1)


if __name__ == '__main__':
    main()
