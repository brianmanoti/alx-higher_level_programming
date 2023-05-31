#!/usr/bin/python3
"""
function to write into a file
"""


def write_file(filename="", text=""):
	"""
		Writes text contents to Filename in str format
	"""
	with open(filename, 'w', encoding='utf-8') as my_file:
		return my_file.write(text)
