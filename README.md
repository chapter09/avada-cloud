<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [0. Requirements](#0-requirements)
  - [0.1 Dependencies](#01-dependencies)
  - [0.2 Notes for hardcode](#02-notes-for-hardcode)
    - [Version](#version)
    - [Spark+Hive+HDFS package](#sparkhivehdfs-package)
    - [VM OS](#vm-os)
    - [EC2](#ec2)
  - [0.3 Todo](#03-todo)
- [1. AWS EC2 Initialization](#1-aws-ec2-initialization)
  - [1.1 Configuration file](#11-configuration-file)
  - [1.2 Deploy key-pair on all regions](#12-deploy-key-pair-on-all-regions)
  - [1.3 Create a security group on all regions](#13-create-a-security-group-on-all-regions)
- [2. EC2 Instances Management](#2-ec2-instances-management)
  - [2.1 How to create instances?](#21-how-to-create-instances)
  - [2.2 How to stop, restart and terminate instances?](#22-how-to-stop-restart-and-terminate-instances)
- [3 Spark+Hive+HDFS Cluster Management](#3-sparkhivehdfs-cluster-management)
  - [3.1 Initializa cluster](#31-initializa-cluster)
  - [3.2 Stop the cluster](#32-stop-the-cluster)
  - [3.3 Restart the whole Spark+Hive+HDFS cluster](#33-restart-the-whole-sparkhivehdfs-cluster)
    - [Stop](#stop)
    - [Start](#start)
  - [3.4 Sync configs on master node to all worker nodes](#34-sync-configs-on-master-node-to-all-worker-nodes)
- [4 Bugs](#4-bugs)
  - [4.1 SSH config](#41-ssh-config)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

#avada-playbook
Ansible playbook for Project Avada

### 0. Requirements

#### 0.1 Dependencies

* Ansible 2.0 (or above)
* python-boto (latest)

#### 0.2 Notes for hardcode
##### Version
    
    Hadoop: 2.6.4
    Spark: 1.6.1
    Hive: 1.2.1

##### Spark+Hive+HDFS package
To enable all the automation ability, please place the software package as below:
  
    avada-playbook/roles/master/files/spark_hdfs_hive.tar.gz

This package will be extracted to the `HOME` directory, and the structure is as below:

    .
    ├── hadoop-2.6.4
    ├── hive-1.2.1
    └── spark-1.6.1

If you want to run Spark **across regions of EC2**, please notice that a patch will be required to apply to `spark-1.6.1`. You could apply the patch `regions.patch` to your directory `spark-1.6.1/core/src`. 

For more information, please refer to [https://github.com/apache/spark/pull/12240/files](https://github.com/apache/spark/pull/12240/files)

##### VM OS
    username: ubuntu

##### EC2
Master instance will be always placed at: 

    region: 'us-east-1'

#### 0.3 Todo

- [ ] To support adding worker nodes incrementally to the existing cluster.
- [ ] Promote the speed of ansible playbook, e.g., introduce `async`.
- [ ] Bug: `cluster_start.yml` might have `rsync` failures.

### 1. AWS EC2 Initialization

#### 1.1 Configuration file
First of all, to enable AWS EC2 access, please add `env` variable `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` to your environment or user profile.

Please modify the configuration files based on the templates first. Files needed to be modified are:
  
    hosts.template
    group_vars
      ├── all.template
      ├── master.template
      └── regions.template

`hosts.template` is empty, just execute `cp hosts.template hosts`. 
#### 1.2 Deploy key-pair on all regions

    ansible-playbook tasks/ec2/ec2_deploy_keys.yml

#### 1.3 Create a security group on all regions
  
    ansible-playbook tasks/ec2/ec2_deploy_securitygroup.yml

### 2. EC2 Instances Management
  
#### 2.1 How to create instances? 
    ansible-playbook -i hosts tasks/ec2/ec2_create_instances.yml

in `group_vars/all` the `vm_num` specifies number of workers in each region. `ec2_launch.yml` will generate `hosts` file automatically.

#### 2.2 How to stop, restart and terminate instances?

    ansible-playbook -i hosts tasks/ec2/ec2_admin.yml -e action=stopped
    ansible-playbook -i hosts tasks/ec2/ec2_admin.yml -e action=running
    ansible-playbook -i hosts tasks/ec2/ec2_admin.yml -e action=absent

### 3 Spark+Hive+HDFS Cluster Management

#### 3.1 Initializa cluster

    ansible-playbook -i hosts site.yml
    ansible-playbook -i hosts tasks/cluster/cluster_start.yml -e init=1

`init=1` is necessary. With it, the HDFS will format its namenode. **If you are not running HDFS for the first time (e.g., after restart the cluster), please remove it!**

In this playbook, we finish the following deployments:

1. Upload the source code of Spark, Hive and HDFS to EC2 `master` node. [ by `roles/master/main.yml` ]
2. Update corresponding configuration of Spark, Hive and HDFS (with public IP of `master` and `workers`. [ by `roles/master/config.yml` ]
3. Sync source code and configuration to all `workers`. [ by `roles/worker/sync.yml` ]
4. Start both HDFS and Spark.

#### 3.2 Stop the cluster
Leave for sleep?

    ansible-playbook -i hosts tasks/ec2/ec2_admin.yml -e action=stopped

#### 3.3 Restart the whole Spark+Hive+HDFS cluster

##### Stop

    ansible-playbook -i hosts tasks/ec2/ec2_admin.yml -e action=stopped

##### Start
    
    ansible-playbook tasks/ec2/ec2_admin.yml -e action=running
    ansible-playbook -i hosts tasks/cluster/cluster_start.yml

#### 3.4 Sync configs on master node to all worker nodes

    ansible-playbook -i hosts tasks/cluster/cluster_sync.yml

### 4 Bugs
#### 4.1 SSH config
    
    ssh -C -q -o ControlMaster=auto -o ControlPersist=60s -o StrictHostKeyChecking=no -o KbdInteractiveAuthentication=no -o PreferredAuthentications=gssapi-with-mic,gssapi-keyex,hostbased,publickey -o PasswordAuthentication=no -o ConnectTimeout=10 -o ControlPath=/home/ubuntu/.ansible/cp/ansible-ssh-%h-%p-%r ec2-54-67-16-133.us-west-1.compute.amazonaws.com
    
    debug3: muxserver_listen: temporary control path /home/ubuntu/.ansible/cp/ansible-ssh-ec2-54-67-16-133.us-west-1.compute.amazonaws.com-22-ubuntu.ubYbuuP8hGfS6YiF unix_listener: "/home/ubuntu/.ansible/cp/ansible-ssh-ec2-54-67-16-133.us-west-1.compute.amazonaws.com-22-ubuntu.ubYbuuP8hGfS6YiF" too long for Unix domain socket

Solution:

in `ansible.cfg`:

    [ssh_connection]
    control_path = /tmp/%%h-%%r
    

