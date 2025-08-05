#!/usr/bin/env python3

import ipdb

def plus_two(num):
    assert plus_two(3) == 5
    num += 2
    ipdb.set_trace()
    return num
