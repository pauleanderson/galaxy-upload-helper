import sys, subprocess, os
dataset = sys.argv[1]
filename = sys.argv[2]
email = sys.argv[3]

galaxy_upload_dir = '/mnt/gv1/galaxy-upload'
email_file_lookup = '/etc/galaxy-upload-helper/emails.txt'

lookup = {}
f = open(email_file_lookup,'r')
lines = f.read().split("\n")
for line in lines:
        fields = line.split(" ")
        if len(fields) >= 2:
                lookup[fields[1]] = fields[0]

cmd = ["cp"] + [dataset] + [galaxy_upload_dir+"/"+email+"/download/"+filename]
result = subprocess.Popen( cmd, stdout=subprocess.PIPE)

stdout, stderr = result.communicate()
if stdout != None:
  print stdout
if stderr != None:
  print >> sys.stderr, stderr

cmd = ["chown"] + [lookup[email]] + [galaxy_upload_dir+"/"+email+"/download/"+filename]
result = subprocess.Popen( cmd, stdout=subprocess.PIPE)
stdout, stderr = result.communicate()

if stdout != None:
  print stdout
if stderr != None:
  print >> sys.stderr, stderr

os.system("touch completed")
