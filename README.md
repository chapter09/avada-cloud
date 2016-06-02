#avada-playbook
Ansible playbook for Project Avada



###How to launch?





###How to stop, restart and terminate?

    ansible-playbook ec2_admin.yml -e action=stopped
    ansible-playbook ec2_admin.yml -e action=restarted
    ansible-playbook ec2_admin.yml -e action=absent

