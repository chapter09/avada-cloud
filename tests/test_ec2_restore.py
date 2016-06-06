from jinja2 import Template

# test instance_list
inlist = [ [
			{
				"ami_launch_index": "0", 
				"architecture": "x86_64", 
				"client_token": "", 
				"ebs_optimized": "false", 
				"groups": [
					{
						"id": "sg-a2a722d9", 
						"name": "hao"
						}
					], 
				"hypervisor": "xen", 
				"id": "i-e9b11475", 
				"image_id": "ami-fce3c696", 
				"instance_profile": "null", 
				"interfaces": [
					{
						"id": "eni-22c91304", 
						"mac_address": "12:7f:4c:47:ef:5b"
						}
					], 
				"kernel": "null", 
				"key_name": "hao-savi-rsa", 
				"launch_time": "2016-06-04T18:48:21.000Z", 
				"monitoring_state": "disabled", 
				"persistent": "false", 
				"placement": {
					"tenancy": "default", 
					"zone": "us-east-1d"
					}, 
				"private_dns_name": "ip-172-31-58-32.ec2.internal", 
				"private_ip_address": "172.31.58.32", 
				"public_dns_name": "ec2-54-89-255-114.compute-1.amazonaws.com", 
				"ramdisk": "null", 
				"region": "us-east-1", 
				"requester_id": "null", 
				"root_device_type": "ebs", 
				"source_destination_check": "true", 
				"spot_instance_request_id": "null", 
				"state": "running", 
				"tags": {
					"Name": "master-hao"
					}, 
				"virtualization_type": "hvm", 
				"vpc_id": "vpc-208ae045"
				}, 
			{
				"ami_launch_index": "0", 
				"architecture": "x86_64", 
				"client_token": "", 
				"ebs_optimized": "false", 
				"groups": [
					{
						"id": "sg-a2a722d9", 
						"name": "hao"
						}
					], 
				"hypervisor": "xen", 
				"id": "i-84b01518", 
				"image_id": "ami-fce3c696", 
				"instance_profile": "null", 
				"interfaces": [
					{
						"id": "eni-60c31946", 
						"mac_address": "12:de:1c:3d:3b:0b"
						}
					], 
				"kernel": "null", 
				"key_name": "hao-savi-rsa", 
				"launch_time": "2016-06-04T20:25:10.000Z", 
				"monitoring_state": "disabled", 
				"persistent": "false", 
				"placement": {
					"tenancy": "default", 
					"zone": "us-east-1d"
					}, 
				"private_dns_name": "ip-172-31-51-73.ec2.internal", 
				"private_ip_address": "172.31.51.73", 
				"public_dns_name": "ec2-52-207-242-229.compute-1.amazonaws.com", 
				"ramdisk": "null", 
				"region": "us-east-1", 
				"requester_id": "null", 
				"root_device_type": "ebs", 
				"source_destination_check": "true", 
				"spot_instance_request_id": "null", 
				"state": "running", 
				"tags": {
					"Name": "worker-hao"
					}, 
				"virtualization_type": "hvm", 
				"vpc_id": "vpc-208ae045"
				}, 
			{
					"ami_launch_index": "1", 
					"architecture": "x86_64", 
					"client_token": "", 
					"ebs_optimized": "false", 
					"groups": [
						{
							"id": "sg-a2a722d9", 
							"name": "hao"
							}
						], 
					"hypervisor": "xen", 
					"id": "i-85b01519", 
					"image_id": "ami-fce3c696", 
					"instance_profile": "null", 
					"interfaces": [
						{
							"id": "eni-61c31947", 
							"mac_address": "12:d9:0a:cb:69:c5"
							}
						], 
					"kernel": "null", 
					"key_name": "hao-savi-rsa", 
					"launch_time": "2016-06-04T18:49:05.000Z", 
					"monitoring_state": "disabled", 
					"persistent": "false", 
					"placement": {
						"tenancy": "default", 
						"zone": "us-east-1d"
						}, 
					"private_dns_name": "ip-172-31-51-74.ec2.internal", 
					"private_ip_address": "172.31.51.74", 
					"public_dns_name": "ec2-54-165-196-140.compute-1.amazonaws.com", 
					"ramdisk": "null", 
					"region": "us-east-1", 
					"requester_id": "null", 
					"root_device_type": "ebs", 
					"source_destination_check": "true", 
					"spot_instance_request_id": "null", 
					"state": "running", 
					"tags": {
						"Name": "worker-hao"
						}, 
					"virtualization_type": "hvm", 
					"vpc_id": "vpc-208ae045"
					}
			], 
	[
			{
				"ami_launch_index": "0", 
				"architecture": "x86_64", 
				"client_token": "", 
				"ebs_optimized": "false", 
				"groups": [
					{
						"id": "sg-a6e957c2", 
						"name": "hao"
						}
					], 
				"hypervisor": "xen", 
				"id": "i-fbdbbc4e", 
				"image_id": "ami-06116566", 
				"instance_profile": "null", 
				"interfaces": [
					{
						"id": "eni-85d56bd8", 
						"mac_address": "06:7e:13:3b:ab:1f"
						}
					], 
				"kernel": "null", 
				"key_name": "hao-savi-rsa", 
				"launch_time": "2016-06-04T18:49:52.000Z", 
				"monitoring_state": "disabled", 
				"persistent": "false", 
				"placement": {
					"tenancy": "default", 
					"zone": "us-west-1a"
					}, 
				"private_dns_name": "ip-172-31-3-187.us-west-1.compute.internal", 
				"private_ip_address": "172.31.3.187", 
				"public_dns_name": "ec2-54-183-89-239.us-west-1.compute.amazonaws.com", 
				"ramdisk": "null", 
				"region": "us-west-1", 
				"requester_id": "null", 
				"root_device_type": "ebs", 
				"source_destination_check": "true", 
				"spot_instance_request_id": "null", 
				"state": "running", 
				"tags": {
					"Name": "worker-hao"
					}, 
				"virtualization_type": "hvm", 
				"vpc_id": "vpc-8e5f14eb"
				}, 
			{
				"ami_launch_index": "1", 
				"architecture": "x86_64", 
				"client_token": "", 
				"ebs_optimized": "false", 
				"groups": [
					{
						"id": "sg-a6e957c2", 
						"name": "hao"
						}
					], 
				"hypervisor": "xen", 
				"id": "i-fadbbc4f", 
				"image_id": "ami-06116566", 
				"instance_profile": "null", 
				"interfaces": [
					{
						"id": "eni-8ad56bd7", 
						"mac_address": "06:51:c2:54:9e:a7"
						}
					], 
				"kernel": "null", 
				"key_name": "hao-savi-rsa", 
				"launch_time": "2016-06-04T18:50:04.000Z", 
				"monitoring_state": "disabled", 
				"persistent": "false", 
				"placement": {
					"tenancy": "default", 
					"zone": "us-west-1a"
					}, 
				"private_dns_name": "ip-172-31-3-188.us-west-1.compute.internal", 
				"private_ip_address": "172.31.3.188", 
				"public_dns_name": "ec2-54-153-83-164.us-west-1.compute.amazonaws.com", 
				"ramdisk": "null", 
				"region": "us-west-1", 
				"requester_id": "null", 
				"root_device_type": "ebs", 
				"source_destination_check": "true", 
				"spot_instance_request_id": "null", 
				"state": "running", 
				"tags": {
					"Name": "worker-hao"
					}, 
				"virtualization_type": "hvm", 
				"vpc_id": "vpc-8e5f14eb"
				}
			], 
	[], 
	[], 
	[], 
	[], 
	[], 
	[], 
	[], 
	[]
]

t_dict = Template("""
		{% for instances in inlist %}
		{% for instance in instances %}
		{% if instance.tags.Name == 'master-hao' %}
		{{ instance.public_dns_name }}
		{% elif instance.tags.Name == 'worker-hao' %}
		{{ instance.public_dns_name }}
		{% endif %}
		{% endfor %}
		{% endfor %}
		""")

print t_dict.render(inlist=inlist)

