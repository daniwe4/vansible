# -*- mode: ruby -*-
# vim: ft=ruby

# ---- Configuration Part -----
NAME = "dawei"

# get IP - addition per defined user 
priv_ip = { 
			"rk" 	=> "0",
 			"sh" 	=> "2",
 			"dawei" => "4",
 			"dk" 	=> "6",
 			"nh" 	=> "8"
 		   }

# virtual machines that will be installed
machines = [ 
			   # "trunk",
			   # "generali",
			   # "seepex",
			   # "panasonic",
			   "mail"
		   ]

nodes = Array.new() { Array.new() }
machines.each_with_index do |serv, index|
	nodes.push( { :hostname => serv, :ip => '192.168.6.' + priv_ip[NAME] + "#{index+2}"} )
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
		ansible.groups = { "webserver" => [""], 
						   "generali" => [""],
						   "mail" => ["mail"] }
	end
end