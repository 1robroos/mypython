#!/home/linuxbrew/.linuxbrew/bin/python3
import json
import boto3
import sys

master_id="i-04a5569b1b43ff406"  # ( Name is Master )
slave_id="i-019baeeba894e973e"

aws_mgmt_con=boto3.session.Session(profile_name="kfsoladmin")
ec2_con_re=aws_mgmt_con.resource(service_name="ec2",region_name="us-east-1")

primary_instance=ec2_con_re.Instance(master_id)
'''
    # See:
    #     EC2¶
    # Table of Contents

    # EC2
    #     Client
    #     Paginators
    #     Waiters
    #     Service Resource
    #     ClassicAddress
    #     DhcpOptions
    #     Image
    #     Instance  <=========================
    
    
# class EC2.Instance(id)
# A resource representing an Amazon Elastic Compute Cloud (EC2) Instance:

#     import boto3

#     ec2 = boto3.resource('ec2')
#     instance = ec2.Instance('id')    


# onder de EC2.Instance object vind je:

# network_interfaces_attribute
#     (list) --

#     [EC2-VPC] The network interfaces for the instance.

#         (dict) --

#         Describes a network interface.

# ........
# ........
'''
#print(primary_instance)
# geeft: ec2.Instance(id='i-059335ab0f5edc2c2')

#print(primary_instance.network_interfaces_attribute)
#geeft:
# [{'Association': {'IpOwnerId': 'amazon', 'PublicDnsName': 'ec2-54-80-33-131.compute-1.amazonaws.com', 'PublicIp': '54.80.33.131'}, 'Attachment': {'AttachTime': datetime.datetime(2022, 2, 27, 11, 13, 30, tzinfo=tzutc()), 'AttachmentId': 'eni-attach-00976b13f49fce650', 'DeleteOnTermination': True, 'DeviceIndex': 0, 'Status': 'attached', 'NetworkCardIndex': 0}, 'Description': '', 'Groups': [{'GroupName': 'launch-wizard-3', 'GroupId': 'sg-0db9998f4aaa28534'}], 'Ipv6Addresses': [], 'MacAddress': '0a:72:b0:f6:db:4f', 'NetworkInterfaceId': 'eni-0d7aa9b54655e49ff', 'OwnerId': '969526043371', 'PrivateDnsName': 'ip-172-31-19-177.ec2.internal', 'PrivateIpAddress': '172.31.19.177', 'PrivateIpAddresses': [{'Association': {'IpOwnerId': 'amazon', 'PublicDnsName': 'ec2-54-80-33-131.compute-1.amazonaws.com', 'PublicIp': '54.80.33.131'}, 'Primary': True, 'PrivateDnsName': 'ip-172-31-19-177.ec2.internal', 'PrivateIpAddress': '172.31.19.177'}, {'Primary': False, 'PrivateDnsName': 'ip-172-31-19-200.ec2.internal', 'PrivateIpAddress': '172.31.19.200'}], 'SourceDestCheck': True, 'Status': 'in-use', 'SubnetId': 'subnet-c5e09e8d', 'VpcId': 'vpc-ebb83a92', 'InterfaceType': 'interface'}]

# Beetje omcatten:

# [
#     {'Association': {'IpOwnerId': 'amazon', 'PublicDnsName': 'ec2-54-80-33-131.compute-1.amazonaws.com', 'PublicIp': '54.80.33.131'
#         }, 
#         'Attachment': {'AttachTime': datetime.datetime(2022,            2,            27,            11,            13,            30, 
#             tzinfo=tzutc()), 'AttachmentId': 'eni-attach-00976b13f49fce650', 'DeleteOnTermination': True, 'DeviceIndex': 0, 'Status': 'attached', 'NetworkCardIndex': 0
#         }, 
#         'Description': '', 'Groups': [
#             {'GroupName': 'launch-wizard-3', 'GroupId': 'sg-0db9998f4aaa28534'
#             }
#         ], 
#         'Ipv6Addresses': [], 
#         'MacAddress': '0a: 72:b0:f6:db: 4f', 'NetworkInterfaceId': 'eni-0d7aa9b54655e49ff', 'OwnerId': '969526043371', 'PrivateDnsName': 'ip-172-31-19-177.ec2.internal', 'PrivateIpAddress': '172.31.19.177', 
#            'PrivateIpAddresses': [
#                 {'Association': {'IpOwnerId': 'amazon', 'PublicDnsName': 'ec2-54-80-33-131.compute-1.amazonaws.com', 'PublicIp': '54.80.33.131'
#                     }, 'Primary': True, 'PrivateDnsName': 'ip-172-31-19-177.ec2.internal', 'PrivateIpAddress': '172.31.19.177'
#                 },
#                 {'Primary': False, 'PrivateDnsName': 'ip-172-31-19-200.ec2.internal', 'PrivateIpAddress': '172.31.19.200'
#                 }
#         ], 'SourceDestCheck': True, 'Status': 'in-use', 'SubnetId': 'subnet-c5e09e8d', 'VpcId': 'vpc-ebb83a92', 'InterfaceType': 'interface'
#     }
# ]

# De 'NetworkCardIndex': 0 :
'''
print(primary_instance.network_interfaces_attribute[0])
'''
# Geeft De dict van de list :
#     {'Association': {'IpOwnerId': 'amazon', 'PublicDnsName': 'ec2-54-80-33-131.compute-1.amazonaws.com', 'PublicIp': '54.80.33.131'
#         }, 
#         'Attachment': {'AttachTime': datetime.datetime(2022,            2,            27,            11,            13,            30, 
#             tzinfo=tzutc()), 'AttachmentId': 'eni-attach-00976b13f49fce650', 'DeleteOnTermination': True, 'DeviceIndex': 0, 'Status': 'attached', 'NetworkCardIndex': 0
#         }, 
#         'Description': '', 'Groups': [
#             {'GroupName': 'launch-wizard-3', 'GroupId': 'sg-0db9998f4aaa28534'
#             }
#         ], 
#         'Ipv6Addresses': [], 
#         'MacAddress': '0a: 72:b0:f6:db: 4f', 'NetworkInterfaceId': 'eni-0d7aa9b54655e49ff', 'OwnerId': '969526043371', 'PrivateDnsName': 'ip-172-31-19-177.ec2.internal', 'PrivateIpAddress': '172.31.19.177', 
#            'PrivateIpAddresses': [
#                 {'Association': {'IpOwnerId': 'amazon', 'PublicDnsName': 'ec2-54-80-33-131.compute-1.amazonaws.com', 'PublicIp': '54.80.33.131'
#                     }, 'Primary': True, 'PrivateDnsName': 'ip-172-31-19-177.ec2.internal', 'PrivateIpAddress': '172.31.19.177'
#                 },
#                 {'Primary': False, 'PrivateDnsName': 'ip-172-31-19-200.ec2.internal', 'PrivateIpAddress': '172.31.19.200'
#                 }
#         ], 'SourceDestCheck': True, 'Status': 'in-use', 'SubnetId': 'subnet-c5e09e8d', 'VpcId': 'vpc-ebb83a92', 'InterfaceType': 'interface'
#     }


#Achter de Networkcardindex[0] kan ik direct van de dict de NetworkInterfaceId opvragen:
print(primary_instance.network_interfaces_attribute[0]['NetworkInterfaceId'])    
# geeft eni-0d7aa9b54655e49ff
#print(primary_instance.state) # {'Code': 16, 'Name': 'running'}
if primary_instance.state['Name']=='running':
    print("Master is running.")
else:
    print("Master is not in  running state")

    slave_instance=ec2_con_re.Instance(slave_id)
    
    master_nic=primary_instance.network_interfaces_attribute[0]['NetworkInterfaceId']
    slave_nic=slave_instance.network_interfaces_attribute[0]['NetworkInterfaceId']
    
    print("master_nic {}".format(master_nic))
    print("slave_nic {}".format(slave_nic))
    
    ha_ip="172.31.58.200"  # ha = high availability 
    
    
    ec2_con_re.meta.client.unassign_private_ip_addresses(
            NetworkInterfaceId=master_nic,
            PrivateIpAddresses=[
            ha_ip,
            ]
    )
    
    ec2_con_re.meta.client.assign_private_ip_addresses(
            NetworkInterfaceId=slave_nic,
            PrivateIpAddresses=[
            ha_ip,
            ]
    )
    
   
    
 