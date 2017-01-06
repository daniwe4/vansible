# File: Vagrantfile

Vagrant.configure("2") do |config|
	config.vm.box = "debian/jessie64"
	config.vm.define "machine1"
	config.vm.define "machine2"

	config.vm.provision :ansible do |ansible|
		ansible.playbook = "playbook.yml"
		ansible.groups = { "webserver" => ["machine[1:2]"],"ilias" => ["machine1"]}
	end
end