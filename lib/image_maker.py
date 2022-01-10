# generates on image to be layered
import math

from PIL import Image, ImageDraw
from random import randint, choice
from lib.cool import hsv2rgb, coin_flip, random_string

shapes = ['rectangle', 'regular_polygon', 'arc']

def make_image(use_func, dimensions):

	[w, h, rows, cols] = dimensions
	w2, h2 = int(w / 2), int(h / 2)

	# get main color
	h1 = randint(0, 360)
	s = randint(33, 100)
	v = randint(33, 100)
	color = hsv2rgb(h1/360, s/100, v/100)

	# create image and graphics draw
	im = Image.new('RGBA', (w, h), (0, 0, 0, 255))
	draw = ImageDraw.Draw(im)

	# set params
	arc_min = [randint(0, 360), randint(0, 360)]
	arc_min.sort()
	arc_max = [randint(0, 360), randint(0, 360)]
	arc_max.sort()

	n_sides_range = [randint(3, 8), randint(3, 8)]
	n_sides_range.sort()

	draw_text = randint(0, 10) > 9 and rows > 32
	draw_alpha_chance = coin_flip()
	modulate = False
	do_mod = coin_flip()
	atan_dir_x = coin_flip()
	atan_order = coin_flip()
	atan_invert = coin_flip()

	x_or_y = coin_flip()
	xy_chance = coin_flip()
	invert = coin_flip()

	shape = choice(shapes)
	func = use_func or choice(funcs)

	size = randint(2, int(w / rows) * 4)
	size2 = int(size / 2)
	random_size = coin_flip()

	# draw shapes
	for c in range(cols):
		for r in range(rows):

			if random_size:
				size = randint(2, int(w / rows) * 4)
				size2 = int(size / 2)

			x = w / cols * c
			y = h / rows * r

			x_, y_ = x, y  # dont change
			_x, _y = x / w,  y / h # 0 - 1 float

			if draw_text:
				if coin_flip():
					text = random_string(randint(2, 5)) if draw_alpha_chance else f"{c}, {r}"
					draw.text([x - size2, y], text, fill=(255,255,255))

			if func == 'random':
				x += randint(0, int(w / cols))
				y += randint(0, int(w / rows))

			if func == 'cos':
				v = 0
				if x_or_y:
					v = math.cos(y)
				else:
					v = math.cos(x)

				if invert:
					v = 1 - v
					modulate = True

				if x_or_y:
					x = v * w2 + w2
				else:
					y = v * h2 + h2

			if func == 'acos':
				v = 0
				if x_or_y:
					v = math.acos(_y)
				else:
					v = math.acos(_x)
				
				if invert:
					v = 1 - v

				if x_or_y:
					x = v * w2 + randint(0, int(w2))
				else:
					y = v * h2 + randint(0, int(h2))

				modulate = True

			if func == 'sin':
				v = 0
				if x_or_y:
					v = math.sin(y)
				else:
					v = math.sin(x)

				if invert:
					v = 1 - v
				modulate = True

				if x_or_y:
					x = v * w2 + w2
				else:
					y = v * h2 + h2

			if func == 'asin':

				v = 0
				x_y = False
				if xy_chance:
					x_y = choice([True, False])
				if x_y or x_or_y:
					v = math.sin(_y)
				else:
					v = math.sin(_x)

				if invert:
					v = 1 - v

				if x_y or x_or_y:
					x = v * w2
					if choice([True, False]):
						x += w2
				else:
					y = v * h2
					if choice([True, False]):
						y += h2

			if func == 'tan':
				if x_or_y or xy_chance:
					x = math.tan(y_) * w2 + w2

				if not x_or_y or xy_chance:	
					y = math.tan(x_) * h2 + h2

				modulate = True

			if func == 'atan':
				if choice([True, False]):
					x = math.atan(y_) * w2
					if choice([True, False]):
						x += w2
				if choice([True, False]):
					y = math.atan(x_) * h2
					if choice([True, False]):
						y += h2 
				modulate = do_mod

			if func == 'atan2':
				v = 0
				if atan_order:
					v = math.atan2(y_, x_)
				else:
					v = math.atan2(x_, y_)

				if atan_invert:
					v = 1 - v

				if atan_dir_x:
					x = v * w2
				else:
					y = v * h2

			if func == 'regular':
				x += size
				y += size

			if x > w:
				# print('x', x)
				if modulate:
					x = x % w
			if y > h:
				# print('y', y)
				if modulate:
					y = y % h

			if shape == 'rectangle':
				draw.rectangle([x - size2, y - size2, x + size2, y + size2], fill=color)
			
			if shape == 'arc':
				start = randint(arc_min[0], arc_min[1])
				end = randint(arc_max[0], arc_max[1])
				width = randint(2, max(2, size2))
				draw.arc([x - size2, y - size2, x + size2, y + size2], start, end, fill=color, width=width)
			
			if shape == 'regular_polygon':
				r = randint(2, size)
				n_sides = randint(n_sides_range[0], n_sides_range[1])
				rotation = randint(0, 360)
				draw.regular_polygon((x - size2, y - size2, r), n_sides, rotation, fill=color)

	return im	