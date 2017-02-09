#!/usr/bin/env python

# Creates the file "playbook.yml"
import yaml
import sys
import os
# from argparse import ArgumentParser

# parser = ArgumentParser(description = "Starts Vagrant")
# parser.add_argument("-m", "--mount", dest="mountvm", action="store_true")
# parser.add_argument("command", metavar="commands", nargs="?", help="commnds piped to vagrant i.e. up/halt/destroy")
# args = parser.parse_args()



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
		config = yaml.load(stream)
	except yaml.YAMLError as exc:
		print(exc)

server_roles = config['server_roles']
password = config['master_pass']

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

def getLines():
	with open("ip.txt") as f:
		return f.readlines()

# get command args without the first (program name)
args 	= sys.argv[1:]
cmd 	= "vagrant " +  " ".join(args)
os.system(cmd)

home_path = os.getenv("HOME")

if "up" in args:
	mkdir = "mkdir -p %s/mount" % (home_path)
	os.system(mkdir)

	if len(args) > 1:
		for arg in args[1:]:
			if arg == "mailer":
				continue
			for line in getLines():
				l = line.rstrip('\n')
				ip.append(l[l.find(' '):].strip())
			ddir = "mkdir -p %s/mount/%s" % (home_path, arg)
			cmd = "echo %s | sshfs -o password_stdin root@%s:/home/vagrant %s/mount/%s" % (password, ip, home_path, arg)
			print cmd + " arg"
			os.system(cmd)
	else:
		for line in getLines():
			l = line.rstrip('\n')
			name = l[:l.find(' ')].strip()
			if name == "mailer":
				continue
			ip = l[l.find(' '):].strip()
			ddir = "mkdir -p %s/mount/%s" % (home_path, name)
			os.system(ddir)
			cmd = "echo %s | sshfs -o password_stdin root@%s:/home/vagrant %s/mount/%s" % (password, ip, home_path, name)
			print cmd
			os.system(cmd)

if ("halt" in args) or ("destroy" in args):
	if len(args) > 1:
		for arg in args[1:]:
			if arg == "mailer":
				continue
			cmd = "umount -f %s/mount/%s" % (home_path, arg)
			print cmd
			os.system(cmd)
	else:
		for line in getLines():
			l = line.rstrip('\n')
			name = l[:l.find(' ')].strip()
			if name == "mailer":
				continue
			cmd = "umount -f %s/mount/%s" % (home_path, name)
			print cmd
			os.system(cmd)

	if not os.listdir("%s/mount/" % (home_path)):
		print "in listdir"
		cmd = "rm -rf %s/mount" % (home_path)
		os.system(cmd)











