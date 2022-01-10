# make a image of text to paste on top

# PIL.Image.NEAREST, PIL.Image.BOX, PIL.Image.BILINEAR, PIL.Image.HAMMING, PIL.Image.BICUBIC or PIL.Image.LANCZOS

from PIL import Image, ImageDraw
from random import randint, choice

cool_words = ['computer', 'apple', 'microsoft', 'keyboard', '1991', 'algorithm', 'artifical', 'bot', 'byte', 'BIOS', 'bit', 'analog', 'adobe', 'binary', 'botnet', 'cookie', 'database', 'datalake', 'debian', 'digital', 'doc', 'email', 'FAT32', 'firewall', 'folder', 'freeware', 'FreeBSD', 'gigabyte', 'hash', 'kernel', 'link', 'motherboard', 'popup', '_blank', 'PRINT', 'QWERTY', 'random access memory', 'root', 'synergy', 'trojan horse', 'system', 'undo', 'delete', 'user', 'version', 'x86', 'embed']

def make_text_image(w, h):
	im = Image.new('RGBA', (int(w / 8), int(h / 16)), (0, 0, 0, 255))
	dr = ImageDraw.Draw(im)
	text = choice(cool_words)
	dr.text([0, 16], text, fill=(255,255,255))
	im = im.resize([w, int(h / 2) + randint(0, int(h / 2))], resample=Image.NEAREST)
	im = im.rotate(randint(0, 360), expand=1, fillcolor=(0, 0, 0))
	im = im.resize([w, h], resample=Image.NEAREST)
	return im