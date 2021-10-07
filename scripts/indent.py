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


def adjust_text(filein, fileout):
	fin = codecs.open(filein, 'r', 'utf-8')
	fout = codecs.open(fileout, 'w', 'utf-8')
	for lin in fin:
		if lin.startswith('<L>'):
			pass
			fout.write(lin)
			entry = ''
		elif lin.startswith('<LEND>'):
			fout.write(entry + '\n' + lin)
		else:
			lin = lin.rstrip()
			entry += lin
	fin.close()
	fout.close()


if __name__ == "__main__":
	filein = sys.argv[1]
	fileout = sys.argv[2]
	adjust_text(filein, fileout)
