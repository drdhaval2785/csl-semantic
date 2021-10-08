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


def insert_tabs(entry, t='\t', l='\n'):
	# Noun section
	entry = entry.replace('{@--Comp.@}', l + '{@--Comp.@}')
	entry = entry.replace('{#--', l + t*2 + '{#--')
	entry = entry.replace('¦ {%', '¦ ' + l + t*2 + '{%')
	entry = re.sub('{%\-\-(.*?)%} ', l + t*2 + '{%--\g<1>%} ' + l + t*4, entry)
	entry = re.sub('\[({.*?)\] ', l + t*3 + '[\g<1>] ' + l + t*4 , entry)
	entry = re.sub('({@\-\-[0-9])', l + t*4 + '\g<1>', entry)
	entry = entry.replace('<P>', l + t*4 + '<P>')
	#entry = re.sub('({%<ab>.*?</ab>%} )', '\g<1>' + l + t*3, entry)
	# Verb section
	entry = re.sub('( {[cv].*?</ab> )({#.*?#} )', l + t + '\g<1>' + l + t*2 + '\g<2>' + l + t*3, entry)
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
			fout.write(entry + '\n' + lin)
		else:
			entry += lin
	fin.close()
	fout.close()


if __name__ == "__main__":
	filein = sys.argv[1]
	fileout = sys.argv[2]
	adjust_text(filein, fileout)
