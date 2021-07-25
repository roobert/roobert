all: record trim

trim:
	gifsicle --crop 0,30-1032,721 t-rec.gif > animation.gif

record:
	t-rec --natural --decor none -e2s ./animation.py

