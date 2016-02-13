#!/usr/bin/env python

""" 
This is python script to extract some useful information from
PHITS makefile and generate CMakeLists.txt

Usage:
     CheckMakefile.py [--phits_dir=<dir>]

Option:
     --phits_dir      set the path of phits directory
     --version, -v    check the version of phits
"""

from sys import argv
from re  import match

# default path of phits directory
phits_dir = "/home/yeyang/Documents/Software/PHITS/phits2.88"

# check the version of this phits code
def GetPhitsVersion(phitsdir):
	return

# check the directory path and get contents of phits makefile
def GetMakefileContents(phits_dir):
	phits_src = phits_dir+"/src"
	phits_makefile = phits_src + "/makefile"
	if (phits_makefile):
		print " -- PHITS Makefile: found"
	else:
		print " -- PHITS Makefile: not found"
	# read makefile and return makfile
	try:
		makefile = open(phits_makefile, "r")
	except:
		print "ERROR: Cannot open this file!! Make sure the directory is correct!!!"
	finally:
		dataline = makefile.readlines()
		makefile.close()
	return dataline

# get source used in this version of phits
def GetSourceInfo(dataline):
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
			GetPhitsVersion(phits_dir)

	print " -- PHITS Directory: ", phits_dir
	contents = GetMakefileContents(phits_dir)
