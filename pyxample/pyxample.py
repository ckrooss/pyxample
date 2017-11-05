#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .lib.common import encode, decode
import logging
FORMAT = '%(asctime)-15s [%(name)s] [%(levelname)s] %(message)s'
logging.basicConfig(format=FORMAT)
log = logging.getLogger(__name__)


def main():
    log.debug("Now in line 11")
    log.info("Runing main()")
    decode(encode("Welcome"))
    log.warn("End of Program")


def cli():
    import argparse
    parser = argparse.ArgumentParser()
    verb = parser.add_mutually_exclusive_group()
    verb.add_argument("-v", "--verbose", help="log more", action='store_true')
    verb.add_argument("-q", "--quiet", help="log less", action='store_true')
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger("pyxample").setLevel(logging.DEBUG)
    elif args.quiet:
        logging.getLogger("pyxample").setLevel(logging.WARN)
    else:
        logging.getLogger("pyxample").setLevel(logging.INFO)

    main()
