#!/usr/bin/python
import getpass
from os import listdir
from os.path import isfile, join
import sys
import os

email_file_lookup = '/mnt/gv1/galaxy-upload/emails.txt'
galaxy_upload_dir = '/mnt/gv1/galaxy-upload'

lookup = {}
f = open(email_file_lookup,'r')
lines = f.read().split("\n")
for line in lines:
	fields = line.split(" ")
	if len(fields) >= 2:
		lookup[fields[0]] = fields[1]

username = getpass.getuser()

if len(sys.argv) < 2:
	print 'usage: upload.py <directory files to upload>'
	exit(1)

mypath = sys.argv[1]
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
for f in onlyfiles:
	os.system("cp "+mypath+"/"+f+" "+galaxy_upload_dir+"/"+lookup[username]+"/")
