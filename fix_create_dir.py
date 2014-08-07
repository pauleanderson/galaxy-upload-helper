#!/usr/bin/python
import os

email_file_lookup = '/etc/galaxy-upload-helper/emails.txt'
galaxy_upload_dir = '/mnt/gv1/galaxy-upload'

f = open(email_file_lookup,'r')
lines = f.read().split("\n")
for line in lines:
        fields = line.split(" ")
        if len(fields) >= 2:
                username = fields[0]
		email = fields[1]
		os.system("mkdir "+galaxy_upload_dir+"/"+email)
		os.system("mkdir "+galaxy_upload_dir+"/"+email+"/download")
		os.system("chown -R "+username+":galaxy "+galaxy_upload_dir+"/"+email)
		os.system("chmod -R gu+rwx "+galaxy_upload_dir+"/"+email)
		os.system("chmod -R o-rwx "+galaxy_upload_dir+"/"+email)

