from jinja2 import Template

input_dict = {
    "ami_launch_index": "0",
    "architecture": "x86_64",
    "block_device_mapping": {
        "/dev/sda1": {
            "delete_on_termination": 'true',
            "status": "attached",
            "volume_id": "vol-64c8a1b4"
        }
    },
    "dns_name": "ec2-54-210-14-178.compute-1.amazonaws.com",
    "ebs_optimized": 'false',
    "groups": {
        "sg-a2a722d9": "hao"
    },
    "hypervisor": "xen",
    "id": "i-7bf821e7",
    "image_id": "ami-fce3c696",
    "instance_type": "t2.micro",
    "kernel": 'null',
    "key_name": "hao-savi-rsa",
    "launch_time": "2016-06-03T04:01:15.000Z",
    "placement": "us-east-1d",
    "private_dns_name": "ip-172-31-62-125.ec2.internal",
    "private_ip": "172.31.62.125",
    "public_dns_name": "ec2-54-210-14-178.compute-1.amazonaws.com",
    "public_ip": "54.210.14.178",
    "ramdisk": 'null',
    "region": "us-east-1",
    "root_device_name": "/dev/sda1",
    "root_device_type": "ebs",
    "state": "running",
    "state_code": 16,
    "tags": {
        "Name": "master-hao"
    },
    "tenancy": "default",
    "virtualization_type": "hvm"
} 

input_list = [
		[
			{
				"ami_launch_index": "0",
				"architecture": "x86_64",
				"block_device_mapping": {
					"/dev/sda1": {
						"delete_on_termination": 'true',
						"status": "attached",
						"volume_id": "vol-952d5945"
						}
					},
				"dns_name": "ec2-54-175-8-152.compute-1.amazonaws.com",
				"ebs_optimized": 'false',
				"groups": {
					"sg-a2a722d9": "hao"
					},
				"hypervisor": "xen",
				"id": "i-942bf108",
				"image_id": "ami-fce3c696",
				"instance_type": "t2.micro",
				"kernel": 'null',
				"key_name": "hao-savi-rsa",
				"launch_time": "2016-06-03T18:46:27.000Z",
				"placement": "us-east-1d",
				"private_dns_name": "ip-172-31-61-19.ec2.internal",
				"private_ip": "172.31.61.19",
				"public_dns_name": "ec2-54-175-8-152.compute-1.amazonaws.com",
				"public_ip": "54.175.8.152",
				"ramdisk": 'null',
				"region": "us-east-1",
				"root_device_name": "/dev/sda1",
				"root_device_type": "ebs",
				"state": "running",
				"state_code": 16,
				"tags": {
					"Name": "worker-hao"
					},
				"tenancy": "default",
				"virtualization_type": "hvm"
				},
			{
				"ami_launch_index": "0",
				"architecture": "x86_64",
				"block_device_mapping": {
					"/dev/sda1": {
						"delete_on_termination": 'true',
						"status": "attached",
						"volume_id": "vol-952d5945"
						}
					},
				"dns_name": "ec2-54-175-8-152.compute-1.amazonaws.com",
				"ebs_optimized": 'false',
				"groups": {
					"sg-a2a722d9": "hao"
					},
				"hypervisor": "xen",
				"id": "i-942bf108",
				"image_id": "ami-fce3c696",
				"instance_type": "t2.micro",
				"kernel": 'null',
				"key_name": "hao-savi-rsa",
				"launch_time": "2016-06-03T18:46:27.000Z",
				"placement": "us-east-1d",
				"private_dns_name": "ip-172-31-61-19.ec2.internal",
				"private_ip": "172.31.61.19",
				"public_dns_name": "ec2-54-175-8-152.compute-1.amazonaws.com",
				"public_ip": "54.175.8.152",
				"ramdisk": 'null',
				"region": "us-east-1",
				"root_device_name": "/dev/sda1",
				"root_device_type": "ebs",
				"state": "running",
				"state_code": 16,
				"tags": {
					"Name": "worker-hao"
					},
				"tenancy": "default",
				"virtualization_type": "hvm"
				}
			]
		] 

t_dict = Template("""{{ worker.public_ip }} {{ '\t' }} # {{ worker.region }}""")
t_list = Template("""{% for region in worker_list %}{% for worker in region %}{{ worker.public_ip }} {{ '\t' }} # {{ worker.region }}
{% endfor %}{% endfor %}""")

print t_dict.render(worker=input_dict)
print t_list.render(worker_list=input_list)

