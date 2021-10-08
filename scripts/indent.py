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
	# Verb section
	entry = re.sub('( {[cv].*?</ab> )({#.*?#} )', l + t + '\g<1>' + l + t*2 + '\g<2>' + l + t*3, entry)
	return entry


def insert_tabs1(entry, l='\n', t='\t'):
	words = re.split('([ ]+)', entry)
	result = ''
	tlevel = 0
	compound = False
	verb = False
	for word in words:
		if re.search('{#\-\-.*?#}', word):
			result += l + t*2 + word
		elif '{%--<ab>' in word:
			result += l + t*2 + word
		elif re.search('<P>', word):
			result += word.replace('<P>', l + t*4 + '<P>')
		elif re.search('^\[', word) and not re.search('^\[Page', word):
			result += l + t*3 + word
		elif re.search('{@[0-9\-]+@}', word):
			result += l + t*4 + word
		else:
			result += word
	return result
	
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
			#entry = insert_tabs(entry)
			entry = insert_tabs1(entry)
			fout.write(entry + '\n' + lin)
		else:
			entry += lin
	fin.close()
	fout.close()


if __name__ == "__main__":
	filein = sys.argv[1]
	fileout = sys.argv[2]
	adjust_text(filein, fileout)
