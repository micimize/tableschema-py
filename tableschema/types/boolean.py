# -*- coding: utf-8 -*-
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import six

from ..config import ERROR

# Module API


def cast_boolean(format, value, **options):
    if not isinstance(value, bool):
        if isinstance(value, six.string_types):
            value = value.strip()
        if value in options.get('trueValues', _TRUE_VALUES):
            value = True
        elif value in options.get('falseValues', _FALSE_VALUES):
            value = False
        else:
            return ERROR
    return value


def uncast_boolean(format, value, **options):
    if not isinstance(value, bool):
        return ERROR
    if value:
        return options.get('trueValues', _TRUE_VALUES)[0]
    else:
        return options.get('falseValues', _FALSE_VALUES)[0]


# Internal

_TRUE_VALUES = ['true', 'True', 'TRUE', '1']
_FALSE_VALUES = ['false', 'False', 'FALSE', '0']
