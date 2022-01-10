# generate an awful nft
from io import BytesIO
from random import randint, choice
from PIL import Image, ImageDraw

from lib.cool import hsv2rgb, coin_flip, random_string
from lib.blend import blend_two
from lib.image_maker import make_image
from lib.text_image import make_text_image

funcs = ['cos',  'sin', 'random', 'regular', 'tan', 'acos', 'asin', 'atan', 'atan2']


def generate_image():
	
	w, h = 512, 512 # image dimensions

	images = []
	num_images = randint(3, 8)
	
	for i in range(num_images):
		f = choice(funcs) # image transform func
		r, c = randint(2, int(w / 4)), randint(2, int( h / 4)) # rows and columns

		n = choice([1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3]) # repeat style chance
		for j in range(n):
			im = make_image(f, [w, h, r, c])
			images.append(im)

	blend = blend_two(images[0], images[1])
	for image in images[2:]:
		blend = blend_two(blend, image)

	# add text
	num_texts = randint(1, 2)
	for i in range(num_texts):
		if coin_flip():
			im = make_text_image(w, h)
			blend = blend_two(blend, im, 'screen')
	
	return blend

def save_jpg(im):
	file_name = f"{random_string(8)}.jpg"
	jpg = Image.new("RGB", im.size, (255, 255, 255))
	jpg.paste(im, mask=im.split()[3]) # 3 is the alpha channel
	# jpg.show()
	jpg.save(f"images/{file_name}", 'JPEG', quality=100)
	return f"images/{file_name}"

def get_image_data():
	im = generate_image()
	file_name = f"{random_string(8)}.jpg"
	jpg = Image.new("RGB", im.size, (255, 255, 255))
	jpg.paste(im, mask=im.split()[3]) # 3 is the alpha channel

	byte_io = BytesIO()
	jpg.save(byte_io, 'JPEG')
	return byte_io

	# got twitter auth error from this

	# with io.BytesIO() as output:
	# 	jpg.save(output, format="JPEG")
	# 	contents = output.getvalue()
	# 	return output.getvalue()

	# https://stackoverflow.com/questions/646286/how-to-write-png-image-to-string-with-the-pil
	# https://stackoverflow.com/questions/47896298/python-api-tweet-with-media-without-file
	# https://stackoverflow.com/questions/43490332/sending-multiple-medias-with-tweepy

if __name__ == '__main__':
	im = generate_image()





