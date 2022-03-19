import boto3
from pprint import pprint
aws_mag_con=boto3.session.Session(profile_name="kfsoladmin")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-1")
#response=ec2_con_cli.describe_instances()
#pprint(response)

#response=ec2_con_cli.describe_instances()['Reservations']
#pprint(response)
# for each_item in response:
#     for each_ii in each_item['Instances']:   # ii = instance info
#         print("The image Id is:{}\nThe Instance ID is: {}\nThe launch time is {}".format(each_ii['ImageId'],each_ii['InstanceId'],each_ii['LaunchTime'].strftime('%Y-%m-%d')))
#         print('x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x')


response=ec2_con_cli.describe_volumes()['Volumes']
#pprint(response)
for each_item in response:
    print("The  volume id is {}\nThe AZ is{}\nThe Volume type is {}".format(each_item['VolumeId'],each_item['AvailabilityZone'],each_item['VolumeType']))
    for each_attment in each_item['Attachments']:
            print("The volume is attached to {}\n" .format(each_attment['InstanceId']))