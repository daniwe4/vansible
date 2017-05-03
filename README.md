
# VANSIBLE
**Vansible provides ILIAS developers with a development environment in a fast and uncomplicated way.**
**This tool uses Vagrant, Ansible and InstILIAS to provide various virtual machines with different software. The developers can do all their settings in a central configuration file.**

**Contact**: [Daniel Weise](https://github.com/daniwe4)

## Usage
### Software Requirements
* Linux or MacOs
* [Vagrant]
* [Ansible]
* [VirtualBox]
* [git]
* [python2.7]
* [pyaml]
* [sshfs]

### Installation
```
$ cd DESTINATION_FOLDER
$ git clone https://github.com/daniwe4/vansible.git
$ cd Vansible
```
### Init 
To init vansible use the following command. It will create a symlink and, so from now on you only need the command "vag".
```
$ sudo ./vag.py
```

### Configuration
All configuration tasks can be done in one file. Open the file $HOME/.vansible/config.yml.


### Next Starts
For all following commands sudo is unnecessary.
If there is only one vm managed by vansible you don´t have to specify the machine name.

Start or Install machines:
```
$ vag up <your_machinename>
```
Stop machines:
````
$ vag halt <your_machinename>
````
Update machines after editing ansible files:
````
$ vag provision <your_machinename>
````
Destroy machines:
````
$ vag destroy <your_machinename>
````

### Access To The Machine

To access to the console of the virtual machine you can use the following command:
````
$ vag ssh <your_machinename>
````
To access the folder structure of the virtual machines i suggest to use sshfs.
````
$ sshfs root@<vm_ip_address>:/home/vagrant/ <mount_dir_on_host>
````

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [Vagrant]: <https://www.vagrantup.com/>
   [Ansible]: <https://www.ansible.com/>
   [VirtualBox]: <https://www.virtualbox.org/>
   [git]: <https://git-scm.com/>
   [python2.7]: <https://www.python.org/downloads/release/python-2713/>
   [pyaml]: <https://pypi.python.org/pypi/pyaml#installation>
   [sshfs]: <https://osxfuse.github.io/>
