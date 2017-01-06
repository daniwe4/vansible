# File: Vagrantfile

Vagrant.configure("2") do |config|
	config.vm.box = "debian/jessie64"
	
	config.vm.define "ILIAS" do |il|
		il.vm.network "forwarded_port", guest: 80, host: 8080
	end

	config.vm.define "GENERALI" do |ge|
		ge.vm.network "forwarded_port", guest: 80, host: 8090
	end

	config.vm.provision :ansible do |ansible|
		ansible.playbook = "playbook.yml"
		ansible.groups = { "webserver" => ["ILIAS", "GENERALI"],"ilias" => ["ILIAS"]}
	end
end