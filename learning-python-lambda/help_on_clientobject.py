from pydoc import describe
import boto3
aws_mag_con=boto3.session.Session(profile_name="kfsoladmin")
# so now I have the mgmt console in a session


iam_con_cli=aws_mag_con.client(service_name="iam",region_name="us-east-1")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-1")
s3_con_cli=aws_mag_con.client(service_name="s3",region_name="us-east-1")

# now list all users, ec2 instances and buckets


# list al IAM users using client object.
response=iam_con_cli.list_users()
#print(response)

#print(response['Users'])

# for each_item in response['Users']:
#     #print(type(each_item))
#     print(each_item['UserName'])


# List all ec2 instance ids
# see boto3 documentation ==> ec2 ==> client. ==> describe_instances
#response=ec2_con_cli.describe_instances()
#print(response)
#print(response['Reservations'])
#print(ec2_con_cli.describe_instances()['Reservations'])

# for each_item in response['Reservations']:
#     print(each_item)
    
# for each_item in response['Reservations']:
#     print(each_item['Instances'])
#     print('=============================')
    
    
# for each_item in response['Reservations']:
#     for each_instance in each_item['Instances']:
#         print(each_instance['InstanceId'])
#     print('=============================')    


##################################################
#List buckets

response=s3_con_cli.list_buckets()
#print(response['Buckets'])


for each_item in response['Buckets']:
    print(each_item['Name'])