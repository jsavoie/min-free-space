#!/usr/bin/python3
import os, sys

def delete_oldest(directory):
	os.chdir(directory)
	files = filter(os.path.isfile, sorted(os.listdir(directory), key=os.path.getmtime))
	if files:
		print ("Deleting file %s" % files[0])
		os.remove(files[0])
	else:
		print ("Nothing to delete")
		sys.exit(1)

def get_used(filesystem):
	fs_stats = os.statvfs(filesystem)
	return (1 - (float(fs_stats.f_bfree) / float(fs_stats.f_blocks))) * 100

filesystem = "/home/media"
directory = "/home/media/backups"
desiredused = 98.0

while get_used(filesystem) > desiredused:
	delete_oldest(directory)
