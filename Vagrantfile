# -*- mode: ruby -*-
# vim: ft=ruby
require 'yaml'


ip_last_part 	= {}
server_groups 	= Hash.new { |hash, key| hash[key] = [] }
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

vars["machines"].each do |index|
	if index['ip'] < 2 || index['ip'] >= 20
		puts "ERROR: Index for your machines are out of range. The allowed range is from 2 to inclusive 19."
		exit
	end

	if index['ip'] >= 10 && index['ip'] < 20
		index['ip'] = index['ip'] - 10
		ip_last_part[NAME] = ip_last_part[NAME].to_i + 1
	end
	machine = NAME + "-" + index['name']
	nodes.push( { :hostname => machine, :ip => ip_first_part + "." + ip_last_part[NAME].to_s + "#{index['ip']}"} )

	unless index['groups'].nil?
		index['groups'].each do |g|
			server_groups[g].push machine
		end
	end
end

# Only use one mail server per subnet
if vars["mailserver"] == true
	nodes.push( { :hostname => 'mailer', :ip => ip_first_part + '.250' } )
end

Vagrant.configure("2") do |config|
	config.vm.box = "debian/jessie64"

	# do for each virtual machine
	nodes.each do |node|
		config.vm.define node[:hostname] do |nodeconfig|
			puts node[:ip]
			nodeconfig.vm.hostname = node[:hostname]
			nodeconfig.vm.network :public_network, ip: node[:ip]
			nodeconfig.vm.provider "virtualbox" do |vb|
				vb.memory = 512
				vb.name = node[:hostname]
			end
		end
	end

	config.vm.provision :ansible do |ansible|
		ansible.playbook = "playbook.yml"
		ansible.groups = server_groups
	end
end