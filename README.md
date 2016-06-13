#avada-playbook
Ansible playbook for Project Avada

###Requirements

* Ansible 2.0 (or above)

### Notes for hardcode
####Version
    
    Hadoop: 2.6.4
    Spark: 1.6.1
    Hive: 1.2.1


####OS
    
    username: ubuntu

####EC2
    
    region: 'us-east-1'


###Initialize the AWS EC2

####Deploy key-pair on all regions

    ansible-playbook tasks/ec2/ec2_deploy_keys.yml

####Create a security group on all regions
  
    ansible-playbook tasks/ec2/ec2_deploy_securitygroup.yml

###How to launch instances?
  
    ansible-playbook -i hosts tasks/ec2/ec2_create_instances.yml -e num=2

`num=2` means lauch 2 workers in each region. `ec2_launch.yml` will generate `hosts` file automatically.

###How to stop, restart and terminate?

    ansible-playbook -i hosts tasks/ec2/ec2_admin.yml -e action=stopped
    ansible-playbook -i hosts tasks/ec2/ec2_admin.yml -e action=running
    ansible-playbook -i hosts tasks/ec2/ec2_admin.yml -e action=absent

###How to start the whole Spark+Hive+HDFS cluster?

####Start

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
    



