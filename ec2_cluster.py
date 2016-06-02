#!/usr/bin/env python
# -*- coding: utf-8 -*-

import boto3
import sys
import os

region_num_map = {
        'us-east-1': 1,
        'us-west-1': 1,
        'us-west-2': 1,
        'eu-west-1': 1,
        'eu-central-1': 1,
        'ap-southeast-1': 1,
        'ap-southeast-2': 1,
        'sa-east-1': 1
        }
launch_type = 'm3.large'
username = 'hao'

ami_map = {
        'us-east-1': 'ami-fce3c696',
        'us-west-1': 'ami-06116566',
        'us-west-2': 'ami-9abea4fb',
        'eu-west-1': 'ami-f95ef58a',
        'eu-central-1': 'ami-87564feb',
        'ap-southeast-1': 'ami-25c00c46',
        'ap-southeast-2': 'ami-6c14310f',
        'sa-east-1': 'ami-0fb83963'
        }

all_regions = ['us-east-1', 'us-west-1', 'us-west-2', 'eu-west-1',
        'eu-central-1', 'ap-southeast-1', 'ap-southeast-2', 'sa-east-1']
active_regions = []
for region in all_regions:
    if region_num_map[region] > 0:
        active_regions.append(region)


conns_ec2 = {}
for region in active_regions:
    conns_ec2[region] = boto3.resource('ec2', region_name=region)

def listAllInstances():
    print "  List All Instances in ./list File\n"
    iplist = open(os.path.abspath(os.path.dirname(sys.argv[0])) + '/list', 'w')
    for region in active_regions:
        conn = conns_ec2[region]
        print "*** Region: %s ***" % region
        for instance in conn.instances.filter(
                Filters=[{'Name': 'instance-type',
                    'Values': [launch_type, 'c4.large']},
                    {'Name': 'tag:Name', 'Values': [username]},
                    {'Name': 'instance-state-name',
                        'Values': ['pending', 'running', 'stopped']}
                    ]):
            iplist.write(instance.public_ip_address + '\n')
            print (instance.id, instance.state['Name'], instance.public_ip_address)

def listRunningInstances():
    print "  List Running Instaces in ./list File\n"
    iplist = open(os.path.abspath(os.path.dirname(sys.argv[0])) + '/list', 'w')
    for region in active_regions:
        conn = conns_ec2[region]
        print "*** Region: %s ***" % region
        for instance in conn.instances.filter(
                Filters=[{'Name': 'instance-type',
                    'Values': [launch_type, 'c4.large']},
                    {'Name': 'tag:Name', 'Values': [username]},
                    {'Name': 'instance-state-name',
                        'Values': ['running']}
                    ]):
            iplist.write(instance.public_ip_address + '\n')
            print (instance.id, instance.state['Name'], instance.public_ip_address)

def launchNewInstances():
    print "  Launching New Instances\n"
    for region_name in active_regions:
        conn = conns_ec2[region_name]
        ami_id = ami_map[region_name]
        count = region_num_map[region_name]
        print "* Region " + region_name + ", count: " + str(count)
        new_instances = conn.create_instances(ImageId=ami_id,
                MinCount=count, MaxCount=count, KeyName=username+'-rsa',
                BlockDeviceMappings=[{
                    'DeviceName': '/dev/sda1',
                    'Ebs': {'VolumeSize':10, 'VolumeType':'gp2'}}],
                InstanceType=launch_type)
        for instance in new_instances:
            instance.create_tags(Tags=[{'Key': "Name", 'Value': username}])

def rebootRunningInstances():
    print "  Rebooting Running Instances\n"
    for region in active_regions:
        conn = conns_ec2[region]
        count = 0
        for instance in conn.instances.filter(
                Filters=[{'Name': 'instance-type', 'Values': [launch_type]},
                    {'Name': 'tag:Name', 'Values': [username]},
                    {'Name': 'instance-state-name',
                        'Values': ['running']}
                    ]):
            instance.reboot()
            count = count + 1
        print "*** Region: %s reboot %d instances ***" % (region, count)


def startStoppedInstancces():
    print "  Starting All Stopped Instances\n"
    for region in active_regions:
        conn = conns_ec2[region]
        count = 0
        for instance in conn.instances.filter(
                Filters=[{'Name': 'instance-type', 'Values': [launch_type]},
                    {'Name': 'tag:Name', 'Values': [username]},
                    {'Name': 'instance-state-name',
                        'Values': ['stopped']}
                    ]):
            instance.start()
            count = count + 1
        print "*** Region: %s start %d instances ***" % (region, count)


def shutdownRunningInstances():
    print "  Shutting Down All Running Instances\n"
    for region in active_regions:
        conn = conns_ec2[region]
        count = 0
        for instance in conn.instances.filter(
                Filters=[{'Name': 'instance-type', 'Values': [launch_type]},
                    {'Name': 'tag:Name', 'Values': [username]},
                    {'Name': 'instance-state-name',
                        'Values': ['running']}
                    ]):
            instance.stop()
            count = count + 1
        print "*** Region: %s stop %d instances ***" % (region, count)


def terminateAllInstances():
    print "  Terminating All Instances\n"
    for region in active_regions:
        conn = conns_ec2[region]
        count = 0
        for instance in conn.instances.filter(
                Filters=[{'Name': 'instance-type', 'Values': [launch_type]},
                    {'Name': 'tag:Name', 'Values': [username]},
                    {'Name': 'instance-state-name',
                        'Values': ['running', 'stopped']}
                    ]):
            instance.terminate()
            count = count + 1
        print "*** Region: %s terminate %d instances ***" % (region, count)

if __name__ == "__main__":
    print "Active Regions: " + str(active_regions)
    command_func_map = {
            "listall": listAllInstances,
            "listrunning": listRunningInstances,
            "launch": launchNewInstances,
            "reboot": rebootRunningInstances,
            "start": startStoppedInstancces,
            "stop": shutdownRunningInstances,
            "terminate": terminateAllInstances
            }

    if len(sys.argv) <= 1:
        print "---------------------------------"
        print " Command Usage:"
        print str(command_func_map.keys())
        print "---------------------------------"
        exit(1)

    for command in sys.argv[1:]:
        if command in command_func_map:
            print "---------------------------------"
            command_func_map[command]()
            print "---------------------------------"

