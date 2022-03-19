import boto3
aws_mag_con=boto3.session.Session(profile_name="kfsoladmin")
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-east-1")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-1")

#print(dir(ec2_con_re.instances))
# geeft:
# 'all', 'create_tags', 'filter', 'iterator', 'limit', 'monitor', 'page_size', 'pages', 'reboot', 'start', 'stop', 'terminate', 'unmonitor']

# om alle instances te starten maar ook om te wachten ( met de waiter )
# tot ze allemaal gestart zijn, moet je alle instance id's hebben:
# define a variable to hold all instance ids:
'''
all_instance_ids=[]
for each_instance in ec2_con_re.instances.all(): # collection object !
    print(each_instance.id) # id valt onder class EC2.Instance(id), zie https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#ec2
    #print(dir(each_instance)) # onder andere id
    all_instance_ids.append(each_instance.id) # append the instance id in this list

# define a waiter
waiter=ec2_con_cli.get_waiter('instance_running')

print("Starting all instances")
ec2_con_re.instances.start()
#dit is niet goed : waiter.wait(InstanceIds=[all_instance_ids]) # 40 checks after every 15 seconds
waiter.wait(InstanceIds=all_instance_ids)  # de variable is al een list, dus hier geen blokhaken zetten.
print("All instances started.")
'''
# nu instances starten aan de hand van de Name tag
# Met de resource obejct heb je geen opties :
#     Request Syntax

# response = ec2.instances.start(
#     AdditionalInfo='string',
#     DryRun=True|False
# )

# Kijk dan naar de client: bij method start_instances() zie je:
# Request Syntax

# response = client.start_instances(
#     InstanceIds=[
#         'string',
#     ],
#     AdditionalInfo='string',
#     DryRun=True|False
# )

# Dus bij die client method kan je instances opgeven.
#bijv als je instance met de naam " non-prod" wil starten:

# create a filter:# Syntax: f1={"Name": "", "Values":[]}
print("------------Filter with resource object -----------------")
nonprod_server_ids=[]
f1={"Name": "tag:Name", "Values":["non-prod"]}
for each_instance  in ec2_con_re.instances.filter(Filters=[f1]):
    #print(each_instance.id)         # id valt onder class EC2.Instance(id), zie https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#ec2
    nonprod_server_ids.append(each_instance.id)
print(nonprod_server_ids)
# gives list ['i-019baeeba894e973e']


# UITLEG over filter en die tag_name:
# filter(**kwargs)
# Creates an iterable of all Instance resources in the collection filtered by kwargs passed to method. A Instance collection will include all resources by default if no filters are provided, and extreme caution should be taken when performing actions on all resources.

# See also: AWS API Documentation

# Request Syntax

# instance_iterator = ec2.instances.filter(
#     Filters=[
#         {
#             'Name': 'string',
#             'Values': [
#                 'string',
#             ]
#         },
#     ],
#     InstanceIds=[
#         'string',
#     ],
#     DryRun=True|False,
#     MaxResults=123,
#     NextToken='string'
# )
#tag:<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key Owner and the value TeamA , specify tag:Owner for the filter name and TeamA for the filter value.
#tag-key - The key of a tag assigned to the resource. Use this filter to find all resources that have a tag with a specific key, regardless of the tag value.


print("------------Now with client object -----------------")
nonprod_server_ids=[]
# filter is nog steeds f1={"Name": "tag:Name", "Values":["non-prod"]}
for each_item in ec2_con_cli.describe_instances(Filters=[f1])['Reservations']:
    for each_in in each_item['Instances']:
        #print(each_in['InstanceId'])
        nonprod_server_ids.append(each_instance.id)
print(nonprod_server_ids)
# This will give a list: ['i-019baeeba894e973e']

ec2_con_cli.start_instances(InstanceIds=nonprod_server_ids)
waiter=ec2_con_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=nonprod_server_ids)  # de variable is al een list, dus hier geen blokhaken zetten.
print("Instances started")
