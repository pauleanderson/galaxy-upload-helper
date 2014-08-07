galaxy-upload-helper
====================

How to use:

0. Please notify Paul Anderson that you want to upload files, so I can add you to the list and configure your directories. This step only needs to be done once.
1. Log into the cluster using your username and password for cluster. Please note that this is separate from the username and password that you use for Galaxy.
2. Upload your file using sftp to a directory of your choosing (. I suggest using a specific upload directory in home directory. You can create one with 'mkdir ~/upload'.
3. Once you've finished uploading your files. Use the following command to put them in a location that Galaxy can see them: upload.py <directory>. For example, if you put your files in ~/upload, then you would type 'upload.py ~/upload'.
4. Now you can go to Galaxy, click 'Get Data'. Then click 'Upload File'. Then select the file of our choice.
