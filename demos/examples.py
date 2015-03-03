#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @file     examples.py
# @author   kaka_ace <xiang.ace@gmail.com>
# @date     Mar 04 2015
# @breif     
#


from useless_utils import FibonacciUtils


for i in range(1, 73):
    result = FibonacciUtils.fibonacci_calculator(i)
    print(result)
