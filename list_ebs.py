#!/home/linuxbrew/.linuxbrew/bin/python3
import boto3
from pprint import pprint
session=boto3.session.Session(profile_name="kfsoladmin")
ec2_client=session.client(service_name="ec2",region_name="us-east-1")

list_volume_ids=[]
filter_prod_backup={"Name":"tag:Prod","Values":["Backup","backup"]}
for each_volume in ec2_client.describe_volumes(Filters=[filter_prod_backup])['Volumes']:
    list_volume_ids.append(each_volume['VolumeId'])
    
print("list of prod voluems :",list_volume_ids)

