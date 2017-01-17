# File: Vagrantfile

Vagrant.configure("2") do |config|
	config.vm.box = "debian/jessie64"

	# config.vm.define "Volker" do |vo|
	# 	vo.vm.hostname = "VOLKER"
	# 	vo.vm.network "public_network", ip: "192.168.6.95", :netmask => "255.255.248.0", :bridge => "en0: Ethernet", :gateway => "192.168.1.1"
	# 	vo.vm.synced_folder "/Users/dw/share/Volker", "/home/vagrant/share", type: "sshfs", create: true
	# end

	# config.vm.define "ILIAS" do |il|
	# 	il.vm.hostname = "ILIAS"
	# 	il.vm.network "private_network", ip: "10.100.0.10"
	# 	# il.vm.network "public_network" , ip: "10.100.0.10", bridge: "en0: Ethernet", use_dhcp_assigned_default_route: "true"
	# 	il.vm.synced_folder "/Users/dw/share/ILIAS", "/home/vagrant/share", type: "sshfs", create: true
	# end

	# config.vm.define "GENERALI" do |ge|
	# 	ge.vm.hostname = "GENERALI"
	# 	ge.vm.network "private_network", ip: "10.100.0.20"
	# 	ge.vm.synced_folder "/Users/dw/share/GENERALI", "/home/vagrant/share", type: "sshfs", create: true
	# end

	config.vm.define "daniel" do |ge|
		ge.vm.hostname = "daniel"
		ge.vm.network "public_network", ip: "192.168.6.93", :netmask => "255.255.248.0", :bridge => "en0: Ethernet", :gateway => "192.168.1.1"
		ge.vm.synced_folder "/Users/dw/share/daniel", "/home/vagrant/share", type: "sshfs", create: true
	end

	config.vm.provision :ansible do |ansible|
		ansible.playbook = "playbook.yml"
		ansible.groups = { "webserver" => ["daniel"]}
	end

	# # Picks up from any failed runs
	# # Run this with: "vagrant provision --provision-with resume"
	# config.vm.provision "resume", type: "ansible" do |resume|
	# 	resume.playbook = "playbook.yml"
	# 	resume.raw_arguments = "--limit @/home/user/playbook.retry"
	# end
end






