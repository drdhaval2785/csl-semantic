# This Python file uses the following encoding: utf-8
"""
Usage:
python indent.py origfile indentedfile
python indent.py ap90.txt ap90_indented.txt
"""
from __future__ import print_function
import re
import codecs
import sys
import os


def remove_line_breaks(entry):
	entry = entry.replace('\n<>', ' ')
	entry = re.sub('[ ]+', ' ', entry)
	entry = entry.replace('\n', '')
	return entry


def insert_tabs(entry, indent='\t'):
	entry = entry.replace('{@--Comp.@}', '\n' + '{@--Comp.@}')
	return entry


def adjust_text(filein, fileout):
	fin = codecs.open(filein, 'r', 'utf-8')
	fout = codecs.open(fileout, 'w', 'utf-8')
	for lin in fin:
		if lin.startswith('<L>'):
			pass
			fout.write(lin)
			entry = ''
		elif lin.startswith('<LEND>'):
			entry = remove_line_breaks(entry)
			entry = insert_tabs(entry)
			fout.write(entry + lin)
		else:
			entry += lin
	fin.close()
	fout.close()


if __name__ == "__main__":
	filein = sys.argv[1]
	fileout = sys.argv[2]
	adjust_text(filein, fileout)
