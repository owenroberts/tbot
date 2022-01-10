# utils

import colorsys
import string
from random import choice


# https://stackoverflow.com/questions/24852345/hsv-to-rgb-color-conversion
def hsv2rgb(h,s,v):
	return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h,s,v))

def coin_flip():
	return choice([True, False])

def random_string(n):
	return ''.join([choice(string.ascii_lowercase) for i in range(n)])

