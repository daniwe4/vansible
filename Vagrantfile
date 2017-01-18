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
		   ]

nodes = Array.new() { Array.new() }
machines.each_with_index do |serv, index|
	nodes.push( { :hostname => serv, :ip => '192.168.6.' + priv_ip[NAME] + "#{index+2}"} )
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
			nodeconfig.vm.synced_folder "/Users/dw/share/#{node[:hostname]}", "/home/vagrant/share", type: "sshfs", create: true
		end
	end

	config.vm.provision :ansible do |ansible|
		ansible.playbook = "playbook.yml"
		ansible.groups = { "webserver" => ["trunk", "generali", "seepex", "panasonic"],
						   "ilias" => ["mailer"],
						   "generali" => ["generali"],
						   "mail" => ["mailer"] }
	end
end