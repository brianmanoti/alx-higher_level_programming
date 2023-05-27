#!/usr/bin/python3


def read_file(filename=""):
""" Opens A file and redirects it as stdout"""
	with open('filename', 'r', encoding='utf-8') as file1:
		data = read(file1)
		print(file1)
