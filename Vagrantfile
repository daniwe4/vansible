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
	ip_last_part[index] = "#{ip}"
end

vars["machines"].each do |index, machine|
	nodes.push( { :hostname => machine, :ip => ip_first_part + "." + ip_last_part[NAME] + "#{index}"} )
end

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
			puts node[:ip]
			nodeconfig.vm.hostname = node[:hostname]
			nodeconfig.vm.network :private_network, ip: node[:ip]
		end
	end

	config.vm.provision :ansible do |ansible|
		ansible.playbook = "playbook.yml"
		ansible.groups = server_groups
	end
end