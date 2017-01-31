#!/usr/bin/env python

# Creates the file "playbook.yml"
import yaml
import sys
import os

if not os.path.isfile("/usr/local/bin/vag"):
	src 	= os.getcwd() + "/vag.py"
	dst 	= "/usr/local/bin/vag"
	os.symlink(src, dst)
	print "Add syslink for {} in {}".format(src, dst)
	sys.exit()

if os.geteuid() == 0:
	print "Please run this script only the first time as root!"
	sys.exit()


# generate a dynamic playbook file
with open("group_vars/all/config.yml", "r") as stream:
	try:
		server_roles = yaml.load(stream)['server_roles']
	except yaml.YAMLError as exc:
		print(exc)

stream	= open("playbook.yml", "w")
stream.write("---\n")
stream.write("# File: playbook.yml\n")

for server_role in server_roles:
	if server_role['roles']:
		stream.write("\n- hosts: {}\n".format(server_role['name']))
		stream.write("  become: yes\n")
		stream.write("  become_method: sudo\n")
		stream.write("  roles:\n")

		for role in server_role['roles']:
			stream.write("    - {}\n".format(role))
	else:
		print("No roles selected for host " + server_role['name'])

stream.close()


# get command args without the first (program name)
args 	= sys.argv[1:]
cmd 	= "vagrant " +  " ".join(args)
# call vagrant with command args
os.system(cmd)
