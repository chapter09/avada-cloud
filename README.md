#avada-playbook
Ansible playbook for Project Avada

###Initialize the AWS EC2

####Deploy key-pair on all regions

    ansible-playbook task/ec2_deploy_keys.yml

####Create a security group on all regions
  
    ansible-playbook task/ec2_deploy_securitygroup.yml

###How to launch instances?
  
    ansible-playbook playbook/ec2_launch.yml -e num=2

`num=2` means lauch 2 workers in each region. `ec2_launch.yml` will generate `hosts` file automatically.

###How to stop, restart and terminate?

    ansible-playbook task/ec2_admin.yml -e action=stopped
    ansible-playbook task/ec2_admin.yml -e action=running
    ansible-playbook task/ec2_admin.yml -e action=absent

###How to restart the whole Spark+Hive+HDFS cluster?

####Stop



####Start
