#avada-playbook
Ansible playbook for Project Avada

###Requirements

* Ansible 2.0 (or above)
* python-boto (latest)

### Notes for hardcode
####Version
    
    Hadoop: 2.6.4
    Spark: 1.6.1
    Hive: 1.2.1


####OS
    
    username: ubuntu

####EC2
    
    region: 'us-east-1'

###Todo

* To support adding worker nodes incrementally to the existing cluster.
* Promote the speed of ansible playbook, e.g., introduce `async`.

###1. AWS EC2 Initialization

####1.1 Configuration file
Please modify the configuration files based on the templates first. Files needed to be modified are:
  
    hosts.template
    group_vars
      ├── all.template
      ├── master.template
      └── regions.template

####1.2 Deploy key-pair on all regions

    ansible-playbook tasks/ec2/ec2_deploy_keys.yml

####1.3 Create a security group on all regions
  
    ansible-playbook tasks/ec2/ec2_deploy_securitygroup.yml

###2. EC2 Instances Management
  
####2.1 How to create instances? 
    ansible-playbook -i hosts tasks/ec2/ec2_create_instances.yml

in `group_vars/all` the `vm_num` specifies number of workers in each region. `ec2_launch.yml` will generate `hosts` file automatically.

####2.2 How to stop, restart and terminate instances?

    ansible-playbook -i hosts tasks/ec2/ec2_admin.yml -e action=stopped
    ansible-playbook -i hosts tasks/ec2/ec2_admin.yml -e action=running
    ansible-playbook -i hosts tasks/ec2/ec2_admin.yml -e action=absent

###3 Spark+Hive+HDFS Cluster Management

####3.1 Initializa cluster

    ansible-playbook -i hosts site.yml
    ansible-playbook -i hosts tasks/cluster/cluster_start.yml -e init=1

In this playbook, we finish the following deployments:

1. Upload the source code of Spark, Hive and HDFS to EC2 `master` node. [ by `roles/master/main.yml` ]
2. Update corresponding configuration of Spark, Hive and HDFS (with public IP of `master` and `workers`. [ by `roles/master/config.yml` ]
3. Sync source code and configuration to all `workers`. [ by `roles/worker/sync.yml` ]

####Stop

    ansible-playbook -i hosts tasks/cluster/cluster_stop.yml

###How to restart the whole Spark+Hive+HDFS cluster?

####Stop

    ansible-playbook tasks/ec2/ec2_admin.yml -e action=stopped

####Start
    
    ansible-playbook tasks/ec2/ec2_admin.yml -e action=running
    ansible-playbook -i hosts tasks/cluster/cluster_start.yml

###Sync configs on master node to all worker nodes

    ansible-playbook -i hosts tasks/cluster/cluster_sync.yml

###Bugs
####SSH config
    
    ssh -C -q -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r ec2-54-67-16-133.us-west-1.compute.amazonaws.com
    
    debug3: muxserver_listen: temporary control path /home/ubuntu/.ansible/cp/ansible-ssh-ec2-54-67-16-133.us-west-1.compute.amazonaws.com-22-ubuntu.ubYbuuP8hGfS6YiF unix_listener: "/home/ubuntu/.ansible/cp/ansible-ssh-ec2-54-67-16-133.us-west-1.compute.amazonaws.com-22-ubuntu.ubYbuuP8hGfS6YiF" too long for Unix domain socket

Solution:

in `ansible.cfg`:

    [ssh_connection]
    control_path = /tmp/%%h-%%r
    



