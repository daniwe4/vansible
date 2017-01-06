# File: Vagrantfile

Vagrant.configure("2") do |config|
	config.vm.box = "debian/jessie64"
	
	config.vm.define "ILIAS" do |il|
		il.vm.hostname = "ILIAS"
		il.vm.network "forwarded_port", guest: 80, host: 8080
		il.vm.synced_folder "/home/dw/share", "/home/ilias/share", type: "sshfs"
	end

	# config.vm.define "GENERALI" do |ge|
	# 	ge.vm.hostname = "GENERALI"
	# 	ge.vm.network "forwarded_port", guest: 80, host: 8090
	# end

	config.vm.provision :ansible do |ansible|
		ansible.playbook = "playbook.yml"
		ansible.groups = { "webserver" => ["ILIAS"],"ilias" => ["ILIAS"]}
	end
end