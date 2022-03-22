#!/home/linuxbrew/.linuxbrew/bin/python3
from logging import Filter
import boto3
from pprint import pprint
session=boto3.session.Session(profile_name="kfsoladmin")
ec2_client=session.client(service_name="ec2",region_name="us-east-1")

list_volume_ids=[]
filter_prod_backup={"Name":"tag:Prod","Values":["Backup","backup"]}
'''
for each_volume in ec2_client.describe_volumes(Filters=[filter_prod_backup])['Volumes']:
    list_volume_ids.append(each_volume['VolumeId'])
    
print("list of prod voluems :",list_volume_ids)
'''

# Paginating needed for when you have more than 50 volumes
paginator = ec2_client.get_paginator('describe_volumes')
response_iterator = paginator.paginate(Filter=[filter_prod_backup])
print(response_iterator) # geeft <botocore.paginate.PageIterator object at 0x7f9e0a811f40>
# we gaan page voor page printen:
for each_page in paginator.paginate(Filters=[filter_prod_backup]):
    pprint(each_page['Volumes']) # Dit geeft weer een list of volumes, paginated.
    # je moet nu nog een extra loop creeren om page by page te iteraten.
    for each_volume in each_page['Volumes']:
        list_volume_ids.append(each_volume['VolumeId'])
    
print("list of prod voluems :",list_volume_ids)
# geeft:
#list of prod voluems : ['vol-09081c14f9b758685', 'vol-027799c646b30338e']


for each_volid in list_volume_ids:
    print("Taking snap of {}".format(each_volid))
    #geeft
    #Taking snap of vol-09081c14f9b758685
    #Taking snap of vol-027799c646b30338e
    

for each_volid in list_volume_ids:
    ec2_client.create_snapshot(
                Description="Taking snapshot with Lambda and CloudWatch",
                VolumeId=each_volid,
                TagSpecifications=[
                    {
                        'ResourceType':'snapshot',
                        'Tags': [
                            {
                                'Key':'Delete-on',
                                'Value':'90'
                            }
                        ]
                    }
                ]
    )
