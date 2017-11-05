#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import logging
FORMAT = '%(asctime)-15s [%(name)s] [%(levelname)s] %(message)s'
logging.basicConfig(format=FORMAT)
log = logging.getLogger(__name__)


def encode(content):
    log.debug("encode()")
    log.debug(content)
    try:
        return json.dumps(content)
    except Exception:
        import traceback
        log.warn(traceback.format_exc())


def decode(content):
    log.debug("decode()")
    log.debug(content)
    try:
        return json.loads(content)
    except Exception:
        import traceback
        log.warn(traceback.format_exc())


def twice(number):
    log.debug("twice()")
    log.debug(number)
    return 2 * number
