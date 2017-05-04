import shutil
import os
import sys


def switchToWorkingDir(file_name):
	""" change to the directory where this file is """
	cur_dir = os.readlink(file_name)
	cur_dir = cur_dir[:cur_dir.rfind("/")]
	os.chdir(cur_dir)

def checkForConfigFiles(path):
	""" check for existing config files
	if exists copy this to group_vars/all/ """
	if not os.path.isdir(path + '/.vansible'):
		os.mkdir(path + "/.vansible", 0755)

	if not os.path.isfile(path + '/.vansible/config.yml'):
		shutil.copy2('./default.yml', path + '/.vansible/config.yml')

	shutil.copy2(path + '/.vansible/config.yml', './group_vars/all/config.yml')

def init():
	src	= os.getcwd() + "/vag.py"
	dst	= "/usr/local/bin/vag"
	os.symlink(src, dst)
	print "Add syslink for %s in %s" % (src, dst)
	sys.exit()