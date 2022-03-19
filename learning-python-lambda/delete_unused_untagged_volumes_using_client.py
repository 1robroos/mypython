import boto3
aws_mag_con=boto3.session.Session(profile_name="kfsoladmin")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-1")

#print(ec2_con_cli.describe_volumes()['Volumes'])
# dit geeft een list:
#[{'Attachments': [], 'AvailabilityZone': 'us-east-1a', 'CreateTime': datetime.datetime(2022, 3, 6, 20, 35, 32, 995000, tzinfo=tzutc()), 'Encrypted': False, 'Size': 1, 'SnapshotId': '', 'State': 'available', 'VolumeId': 'vol-047eb25fa2a777364', 'Iops': 100, 'Tags': [{'Key': 'purpose', 'Value': 'test - kan weg'}], 'VolumeType': 'gp2', 'MultiAttachEnabled': False}, {'Attachments': [], 'Avail
'''
for each_item in ec2_con_cli.describe_volumes()['Volumes']:
    print(each_item)
'''
# geeft een dict:
#{'Attachments': [{'AttachTime': datetime.datetime(2022, 2, 2, 14, 1, 18, tzinfo=tzutc()), 'Device': '/dev/sda1', 'InstanceId': 'i-019baeeba894e973e', 'State': 'attached', 'VolumeId': 'vol-09081c14f9b758685', 'DeleteOnTermination': True}], 'AvailabilityZone': 'us-
# in die dict zie je ook : 'VolumeId': 'vol-027799c646b30338e'
# opvragen met:
'''
for each_item in ec2_con_cli.describe_volumes()['Volumes']:
    print(each_item['VolumeId'],each_item['Tags'])
'''
#Dit kan niet , want niet ieder volume heeft een tag, en dan kan je die niet uitvragen. De error is:
#     print(each_item['VolumeId'],each_item['Tags'])
# KeyError: 'Tags'
'''
for each_item in ec2_con_cli.describe_volumes()['Volumes']:
    if not "Tags" in each_item:
        print(each_item['VolumeId'])
'''
print("Going to delete unused and untagged volumes")
for each_item in ec2_con_cli.describe_volumes()['Volumes']:
    if not "Tags" in each_item and each_item['State']=='available':
        print("Deleting" ,each_item['VolumeId']) 
        ec2_con_cli.delete_volume(VolumeId=each_item['VolumeId']) 
print("Deleted unused and untagged volumes")
   
# # this gives:
# Going to delete unused and untagged volumes
# Deleting vol-0462a82fb600fbec3
# Deleted unused and untagged volumes 
