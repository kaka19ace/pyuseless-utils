#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @file     generators
# @author   kaka_ace <xiang.ace@gmail.com>
# @date     Mar 04 2015
# @breif     
# 


import sys
if sys.version_info < (3, 0):
    range = xrange
else:
    from functools import reduce

import math

from contextlib import contextmanager


class FibonacciUtils(object):
    @staticmethod
    def fibonacci_calculator(n):
        """
        if n == 0:
            raise ValueError("")
        if n == 1:
            return 0


        :param n: integer, cacalute the nth value

        inspired from:
        http://stackoverflow.com/questions/4935957/fibonacci-numbers-with-an-one-liner-in-python-3

        :return: the last result value
        """
        if n == 0:
            raise ValueError("")
        if n == 1:
            return 0

        if n <= 71:
            # when n is 72, the formula could not be used, because of the precision problems
            return int(((1 + math.sqrt(5)) / 2) ** (n-1) / math.sqrt(5) + 0.5)

        # i must set to 3
        i, g = 3, FibonacciGenartors.fibonacci()
        while i < n:
            i += 1
            next(g)
        v = next(g)
        g.close()
        return v

    @staticmethod
    def fibonacci():
        """
        init with 0, 1
        :return: generator function
        """
        a, b = 0, 1
        while True:
            yield a + b
            a, b = b, a + b

    @staticmethod
    def get_fibonacci_generator():
        """
        init with 0, 1
        :return: generator
        """
        return FibonacciGenartors.fibonacci()