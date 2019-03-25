# -*- coding: utf-8 -*-


def get_two_float(f_str):
    f_str = str(f_str)
    a, b, c = f_str.partition('.')
    c = c[:2]
    return float(".".join([a, c]))
