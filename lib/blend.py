# blend images

import blend_modes
import numpy
from PIL import Image
from random import choice

blend_mode_types = [
	'addition', 'darken_only', 'difference', 'divide', 'dodge', 'grain_extract', 'grain_merge', 'hard_light', 'lighten_only', 'multiply', 'normal', 'overlay', 'screen', 'soft_light', 'subtract'
]

sub_types = [
	'addition', 'difference', 'dodge', 'grain_extract', 'grain_merge', 'lighten_only', 'overlay', 'screen', 'soft_light'
]

def get_im_float(im):
	a = numpy.array(im)
	f = a.astype(float)
	return f

def blend_two(a, b, m=None):
	af = get_im_float(a)
	bf = get_im_float(b)
	mode = m or choice(sub_types)
	# print('blend mode', mode)
	mode_f = getattr(blend_modes, mode)
	blendf = mode_f(af, bf, 1)
	blendi = numpy.uint8(blendf)
	blend = Image.fromarray(blendi)
	return blend