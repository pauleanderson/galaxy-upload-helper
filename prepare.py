import sys, subprocess, os
dataset = sys.argv[1]
filename = sys.argv[2]
email = sys.argv[3]

galaxy_download_dir = '/mnt/gv1/galaxy-download'
email_file_lookup = '/mnt/gv1/galaxy-upload/emails.txt'

lookup = {}
f = open(email_file_lookup,'r')
lines = f.read().split("\n")
for line in lines:
        fields = line.split(" ")
        if len(fields) >= 2:
                lookup[fields[1]] = fields[0]

cmd = ["ln"] + [dataset] + [galaxy_download_dir+"/"+email+"/"+filename]
result = subprocess.Popen( cmd, stdout=subprocess.PIPE)

stdout, stderr = result.communicate()
if stdout != None:
  print stdout
if stderr != None:
  print >> sys.stderr, stderr

#cmd = ["chown"] + [lookup[email]+":"+lookup[email]] + [galaxy_download_dir+"/"+email+"/"+filename]
#result = subprocess.Popen( cmd, stdout=subprocess.PIPE)
#stdout, stderr = result.communicate()

#if stdout != None:
#  print stdout
#if stderr != None:
#  print >> sys.stderr, stderr

os.system("touch completed")
