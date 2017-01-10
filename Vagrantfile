# File: Vagrantfile

Vagrant.configure("2") do |config|
	config.vm.box = "debian/jessie64"
	
	config.vm.define "ILIAS" do |il|
		il.vm.hostname = "ILIAS"
		il.vm.network "forwarded_port", guest: 80, host: 8080
		il.vm.synced_folder "/Users/dw/share/ILIAS", "/home/vagrant/share", type: "sshfs", create: true
	end

	config.vm.define "GENERALI" do |ge|
		ge.vm.hostname = "GENERALI"
		ge.vm.network "forwarded_port", guest: 80, host: 8090
		ge.vm.synced_folder "/Users/dw/share/GENERALI", "/home/vagrant/share", type: "sshfs", create: true
	end

	config.vm.define "SEEPEX" do |ge|
		ge.vm.hostname = "SEEPEX"
		ge.vm.network "forwarded_port", guest: 80, host: 8100
		ge.vm.synced_folder "/Users/dw/share/SEEPEX", "/home/vagrant/share", type: "sshfs", create: true
	end

	config.vm.provision :ansible do |ansible|
		ansible.playbook = "playbook.yml"
		ansible.groups = { "webserver" => ["ILIAS", "GENERALI", "SEEPEX"] }
	end
end