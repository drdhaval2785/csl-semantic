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


if __name__ == "__main__":
	filein = sys.argv[1]
	fileout = sys.argv[2]
	fin = codecs.open(filein, 'r', 'utf-8')
	fout = codecs.open(fileout, 'w', 'utf-8')
	for lin in fin:
		if lin.startswith('<L>'):
			pass
			fout.write(lin)
		elif lin.startswith('<LEND>'):
			fout.write('\n' + lin)
		else:
			lin = lin.rstrip()
			fout.write(lin)
	fin.close()
	fout.close()

