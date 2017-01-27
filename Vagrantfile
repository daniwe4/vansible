# -*- mode: ruby -*-
# vim: ft=ruby

# ---- Configuration Part -----
require 'yaml'

ip_last_part 	= {}
server_groups 	= {}
nodes 			= Array.new() { Array.new() }
vars 			= YAML.load_file('group_vars/all/config.yml')
ip_first_part 	= vars['ip_first_part']
NAME 			= vars["name"]


vars["user"].each do |index, ip|
	if ip < 0 || ip > 22
		puts "ERROR: User number is out of range. The allowed range is from 0 to inclusive 22."
		exit
	end

	if ip == 0
		ip_last_part[index] = ""
	else
		ip_last_part[index] = "#{ip}"
	end
end

vars["machines"].each do |index, machine|
	if index < 2 || index >= 20
		puts "ERROR: Index for your machines are out of range. The allowed range is from 2 to inclusive 19."
		exit
	end

	if index >= 10 && index < 20
		index = index - 10
		ip_last_part[NAME] = ip_last_part[NAME].to_i + 1
	end
	nodes.push( { :hostname => machine, :ip => ip_first_part + "." + ip_last_part[NAME].to_s + "#{index}"} )
end
puts nodes
vars["groups"].each do |index, group|
	server_groups[index] = group
end

# Only use one mail server per subnet
if vars["mailserver"] == true
	nodes.push( { :hostname => 'mailer', :ip => ip_first_part + '.250' } )
end

Vagrant.configure("2") do |config|
	# configurate VirtualBox
	config.vm.provider "virtualbox" do |vb|
		vb.memory = 512
	end

	config.vm.box = "debian/jessie64"

	# do for each virtual machine
	nodes.each do |node|
		config.vm.define node[:hostname] do |nodeconfig|
			#puts node[:ip]
			#config.vm.name = NAME + "-" + node[:hostname]
			nodeconfig.vm.hostname = node[:hostname]
			nodeconfig.vm.network :private_network, ip: node[:ip]
		end
	end

	config.vm.provision :ansible do |ansible|
		ansible.playbook = "playbook.yml"
		ansible.groups = server_groups
	end
end