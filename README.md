#avada-playbook
Ansible playbook for Project Avada



###How to launch?
  
    ansible-playbook playbook/ec2_launch.yml -e num=2

`num=2` means lauch 2 workers in each region.

###How to stop, restart and terminate?

    ansible-playbook playbook/ec2_admin.yml -e action=stopped
    ansible-playbook playbook/ec2_admin.yml -e action=running
    ansible-playbook playbook/ec2_admin.yml -e action=absent

