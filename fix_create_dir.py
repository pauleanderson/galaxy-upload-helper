#!/usr/bin/python
import os

email_file_lookup = '/mnt/gv1/galaxy-upload/emails.txt'
galaxy_upload_dir = '/mnt/gv1/galaxy-upload'
galaxy_download_dir = '/mnt/gv1/galaxy-download'
user_dir = '/mnt/gv1/users'

f = open(email_file_lookup,'r')
lines = f.read().split("\n")
for line in lines:
        fields = line.split(" ")
        if len(fields) >= 2:
                username = fields[0]
		email = fields[1]
		if not os.path.isdir(galaxy_upload_dir+"/"+email):
			os.system("mkdir "+galaxy_upload_dir+"/"+email)
		if not os.path.isdir(galaxy_download_dir+"/"+email):
			os.system("mkdir "+galaxy_download_dir+"/"+email)
		if not os.path.isdir(user_dir+"/"+username):
			os.system("mkdir "+user_dir+"/"+username)
		os.system("chown "+username+":galaxy "+galaxy_upload_dir+"/"+email)
		os.system("chown "+username+":galaxy "+galaxy_download_dir+"/"+email)
		os.system("chown "+username+":"+username+" "+user_dir+"/"+username)
		os.system("chmod -R gu+srw "+galaxy_upload_dir+"/"+email)
		os.system("chmod -R o-rwx "+galaxy_upload_dir+"/"+email)
		os.system("chmod gu+srwx "+galaxy_download_dir+"/"+email)
		os.system("chmod o-rwx "+galaxy_download_dir+"/"+email)

