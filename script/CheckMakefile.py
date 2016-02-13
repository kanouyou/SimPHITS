#!/usr/bin/env python

""" 
This is python script to extract some useful information from
PHITS makefile and generate CMakeLists.txt

Usage:
     CheckMakefile.py [--option]

Option:
     --phits_dir      set the path of phits directory
     --version, -v    check the version of phits
     --silent, -s     silent mode
"""

from sys import argv
from re  import match

fSilent = False

# default path of phits directory
phits_dir = "/home/yeyang/Documents/Software/PHITS/phits2.88"

# check the version of this phits code
def GetPhitsVersion(phitsdir):
	version = 0.0
	phits_main = phitsdir + "/src/main.f"
	try:
		mainfile = open(phits_main, "r")
	except:
		print "ERROR: Cannot open this file: ", phits_main
		print "NOTE: Please make sure if this file exsits or not!!"
	finally:
		dataline = mainfile.readlines()
		mainfile.close()
		# check the version
		for eachline in dataline:
			if match("^\s+ parameter \( Version =", eachline):
				eachline.strip()
				item = eachline.split()
				version = item[4]
	return version

# check the directory path and get contents of phits makefile
def GetMakefileContents(phits_dir):
	phits_src = phits_dir+"/src"
	phits_makefile = phits_src + "/makefile"
	if (fSilent==False):
		if (phits_makefile):
			print " -- PHITS Makefile: found"
		else:
			print " -- PHITS Makefile: not found"
	# read makefile and return makfile
	try:
		makefile = open(phits_makefile, "r")
	except:
		print "ERROR: Cannot open this file: ", phits_makefile
		print "NOTE: Please make sure if this file exsits or not!!"
	finally:
		dataline = makefile.readlines()
		makefile.close()
	return dataline

# get source used in this version of phits
def GetSourceInfo(dataline):
	src = []
	# read makefile contents
	for i in range(len(dataline)):
		if match("^SRCS[0-9]", dataline[i]):
			# src buffer to contain the info
			buff = []
			# read next 10 lines after this line
			for j in range(10):
				# input info into buffer until found "^$"
				if match("^$", dataline[i+j]):
					break
				buff.append(dataline[i+j])
			src.append(buff)
	for i in range(len(src)):
		for j in range(len(src[i])):
			ben = src[i][j].strip().strip("\\")
			item = ben.split()
			print item
	return


# ----------- main ------------- #
if (__name__=="__main__"):
	# update the phits directory info first
	for i in range(len(argv)):
		if (match("--phits_dir=", argv[i])):
			phits_dir = argv[i][12:]
	# check the other option
	for i in range(len(argv)):
		if (argv[i]=="--version" or argv[i]=="-v"):
			version = GetPhitsVersion(phits_dir)
			print " -- PHITS Version: ", version
		elif (argv[i]=="--silent" or argv[i]=="-s"):
			fSilent = True

	if (fSilent==False):
		print " -- PHITS Directory: ", phits_dir
	contents = GetMakefileContents(phits_dir)
	GetSourceInfo(contents)
