import sys, subprocess, os
dataset = sys.argv[1]
filename = sys.argv[2]
email = sys.argv[3]

galaxy_upload_dir = '/mnt/gv1/galaxy-upload'

cmd = ["cp"] + [dataset] + [galaxy_upload_dir+"/"+email+"/download/"+filename]
result = subprocess.Popen( cmd, stdout=subprocess.PIPE)

stdout, stderr = result.communicate()
stdout += "Command:\n"
stdout += " ".join(cmd)

print "Standard out: "
print stdout
print "Standard error: "
print stderr

os.system("touch completed")
