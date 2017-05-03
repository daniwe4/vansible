#!/usr/bin/env python

import yaml
import sys
import os
import init

home_path = os.getenv("HOME")
out = "***VAG-->"

def getMachineDict():
	"""getMachineDict()"""
	machine_dict = {}
	with open("ip.txt") as f:
		for line in f.readlines():
			l = line.rstrip('\n')
			machine_dict[l[:l.find(' ')].strip()] = l[l.find(' '):].strip()
	return machine_dict

def getMachineNames():
	"""
	get a list of names from the created machines
	"""
	names = []
	for key in getMachineDict():
		names.append(key)
	return ' '.join(names)

def getRelevantIp(machine):
	"""getRelevantIp(machine)"""
	machine_dict = getMachineDict()
	for key in machine_dict:
		if machine == key:
			return machine_dict[key]
	return None

def getVagrantCommand(args):
	"""getVagrantCommand(args)"""
	if len(args) > 1:
		return args[1]
	return None

def getOptionalCommands(args):
	"""getOptionalCommands(args)"""
	opt_commands = []
	if len(args) > 2:
		for arg in args[2:]:
			opt_commands.append(arg)
		return opt_commands
	return None

def mountMachines(machines):
	"""mountMachines(machines)"""
	machines = machines.split()

	for machine in machines:
		if "mailer" == machine:
			continue
		ip = getRelevantIp(machine)
		create_path = "mkdir -p %s/mount/%s" % (home_path, machine)
		os.system(create_path)
		print "%s Add folder %s/mount/%s" % (out, home_path, machine)
		cmd = "echo %s | sshfs -o password_stdin root@%s:/home/vagrant %s/mount/%s" % (password, ip, home_path, machine)
		os.system(cmd)
		print "%s Mount %s to %s/mount/%s" % (out, machine, home_path, machine)

def umountMachines(machines):
	"""umountMachines(machines)"""
	machines = machines.split()
	for machine in machines:
		if "mailer" == machine:
			continue
		cmd = "umount %s/mount/%s" % (home_path, machine)
		os.system(cmd)
		print "%s Unmount %s from %s/mount/%s" % (out, machine, home_path, machine)
		cmd = "rm -rf %s/mount/%s" % (home_path, machine)
		os.system(cmd)
		print "%s Remove folder %s/mount/%s" % (out, home_path, machine)
	if not os.listdir("%s/mount/" % (home_path)):
		cmd = "rm -rf %s/mount" % (home_path)
		os.system(cmd)
		print "%s Remove folder %s/mount" % (out, home_path)

def callVagrant(cmd, opt):
	"""callVagrant(cmd, opt)"""
	cmdline = "vagrant %s %s" % (cmd, opt)
	os.system(cmdline)

def usage():
	"""usage()"""
	print "Usage: vag <vagrant_command> [[<machine_name>] ...]"

def handleCommands(vag_command, opt_commands):
	"""handleCommands(vag_command, opt_commands)"""
	if (opt_commands != None) and (len(opt_commands) > 0):
		machines = ' '.join(opt_commands)
	else:
		machines = getMachineNames();

	if vag_command != None:
		if "up" in vag_command:
			callVagrant("up", machines)
			#mountMachines(machines)
		elif "halt" in vag_command:
			#umountMachines(machines)
			callVagrant("halt", machines)
		elif "destroy" in vag_command:
			#umountMachines(machines)
			callVagrant("destroy", machines)
		elif "ssh" in vag_command:
			callVagrant("ssh", machines)
		elif "provision" in vag_command:
			callVagrant("provision", machines)
		else:
			print "Unknown command"
	else:
		usage()

def loadYaml(filename):
	# generate a dynamic playbook file
	with open(filename, "r") as stream:
		try:
			config = yaml.load(stream)
		except yaml.YAMLError as exc:
			print(exc)
	return config

def generatePlaybook():
	stream = open("playbook.yml", "w")
	stream.write("---\n")
	stream.write("# File: playbook.yml\n")

	for server_role in server_roles:
		if server_role['roles']:
			stream.write("\n- hosts: %s\n" % (server_role['name']))
			stream.write("  become: yes\n")
			stream.write("  become_method: sudo\n")
			stream.write("  roles:\n")

			for role in server_role['roles']:
				stream.write("    - %s\n" % (role))
		else:
			print("No roles selected for host %s" % (server_role['name']))
	stream.close()

if not os.path.isfile("/usr/local/bin/vag"):
	init.init(home_path)


if os.geteuid() == 0:
	print "Please run this script only the first time as root!"
	sys.exit()

init.switchToWorkingDir(__file__)
init.checkForConfigFiles(home_path);
if not os.path.isfile(os.getcwd() + "/ip.txt"):
	file = open("ip.txt", "w")
config = loadYaml("group_vars/all/config.yml")
server_roles = config['server_roles']
password = config['master_pass']
generatePlaybook()
handleCommands(getVagrantCommand(sys.argv), getOptionalCommands(sys.argv))