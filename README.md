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

###Initialize the AWS EC2

####Deploy key-pair on all regions

    ansible-playbook tasks/ec2/ec2_deploy_keys.yml

####Create a security group on all regions
  
    ansible-playbook tasks/ec2/ec2_deploy_securitygroup.yml

###How to launch instances?
  
    ansible-playbook tasks/ec2/ec2_create_instances.yml -e num=2

`num=2` means lauch 2 workers in each region. `ec2_launch.yml` will generate `hosts` file automatically.

###How to stop, restart and terminate?

    ansible-playbook tasks/ec2/ec2_admin.yml -e action=stopped
    ansible-playbook tasks/ec2/ec2_admin.yml -e action=running
    ansible-playbook tasks/ec2/ec2_admin.yml -e action=absent

###How to start the whole Spark+Hive+HDFS cluster?

####Start

    ansible-playbook -i hosts site.yml

In this playbook, we finish the following deployments:

1. Upload the source code of Spark, Hive and HDFS to EC2 `master` node. [ by `roles/master/main.yml` ]
2. Update corresponding configuration of Spark, Hive and HDFS (with public IP of `master` and `workers`. [ by `roles/master/config.yml` ]
3. Sync source code and configuration to all `workers`. [ by `roles/worker/sync.yml` ]

###How to restart the whole Spark+Hive+HDFS cluster?

####Stop

    ansible-playbook tasks/ec2/ec2_admin.yml -e action=stopped


####Start
    
    ansible-playbook tasks/ec2/ec2_admin.yml -e action=running

