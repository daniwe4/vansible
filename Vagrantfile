# -*- mode: ruby -*-
# vim: ft=ruby

# ---- Configuration Part -----
require 'yaml'

# get IP - addition per defined user 
priv_ip = {}
server_groups = {}
nodes = Array.new() { Array.new() }
vars = YAML.load_file('group_vars/all/config.yml')

NAME = vars["name"]

vars["user"].each do |index, ip|
	priv_ip[index] = "#{ip}"
end

vars["machines"].each do |index, machine|
	nodes.push( { :hostname => machine, :ip => '192.168.6.' + priv_ip[NAME] + "#{index}"} )
end

vars["groups"].each do |index, group|
	server_groups[index] = group
end

# Only use one mail server per ip range
nodes.push( { :hostname => 'mailer', :ip => '192.168.6.250' } )

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
		ansible.limit = "all"
		ansible.groups = server_groups
	end
end