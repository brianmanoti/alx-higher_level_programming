#!/usr/bin/python3


def read_file(filename=""):
""" Opens A file and redirects it as stdout"""
	with open('filename', encoding='utf-8') as f:
		for line in f:
			print(line)
