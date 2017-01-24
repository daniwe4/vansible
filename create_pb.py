#!/usr/bin/env python

# Creates the file "playbook.yml"
import yaml

with open("group_vars/all/config.yml", "r") as stream:
	try:
		server_roles = yaml.load(stream)['server_roles']
	except yaml.YAMLError as exc:
		print(exc)

stream = open("playbook.yml", "w")
stream.write("---\n")
stream.write("# File: playbook.yml\n")

for server_role in server_roles:
	stream.write("\n- hosts: {}\n".format(server_role['name']))
	stream.write("  become: yes\n")
	stream.write("  become_method: sudo\n")
	stream.write("  roles:\n")

	for role in server_role['roles']:
		stream.write("    - {}\n".format(role))

stream.close()
