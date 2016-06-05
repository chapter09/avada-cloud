#avada-playbook
Ansible playbook for Project Avada

###Initialize the AWS EC2

####Deploy key-pair on all regions

    ansible-playbook tasks/ec2_deploy_keys.yml

####Create a security group on all regions
  
    ansible-playbook tasks/ec2_deploy_securitygroup.yml

###How to launch instances?
  
    ansible-playbook tasks/ec2_create_instances.yml -e num=2

`num=2` means lauch 2 workers in each region. `ec2_launch.yml` will generate `hosts` file automatically.

###How to stop, restart and terminate?

    ansible-playbook tasks/ec2_admin.yml -e action=stopped
    ansible-playbook tasks/ec2_admin.yml -e action=running
    ansible-playbook tasks/ec2_admin.yml -e action=absent

###How to restart the whole Spark+Hive+HDFS cluster?

####Stop

    ansible-playbook tasks/ec2_admin.yml -e action=stopped


####Start
    
    ansible-playbook tasks/ec2_admin.yml -e action=running

