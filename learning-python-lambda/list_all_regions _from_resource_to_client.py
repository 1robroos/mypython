import boto3
aws_mag_con=boto3.session.Session(profile_name="kfsoladmin")
ec2_con_re=aws_mag_con.resource(service_name="ec2")
print(dir(ec2_con_re))
print(dir(ec2_con_re.meta))
print(ec2_con_re.meta.client.describe_regions())
print(ec2_con_re.meta.client.describe_regions()['Regions'])
for each_item in ec2_con_re.meta.client.describe_regions()['Regions']:
    print(each_item['RegionName'])