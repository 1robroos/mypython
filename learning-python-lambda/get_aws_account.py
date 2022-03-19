#import profile
import boto3
aws_mag_con=boto3.session.Session(profile_name="kfsoladmin")
sts_con_cli=aws_mag_con.client(service_name="sts",region_name="us-east-1")
response =sts_con_cli.get_caller_identity()
print(response)


aws_mag_con_eksdude=boto3.session.Session(profile_name="eksdude")
sts_con_cli=aws_mag_con_eksdude.client(service_name="sts",region_name="us-east-1")
response =sts_con_cli.get_caller_identity()
print(response)
print(response['Account'])
print(response.get('Account'))
