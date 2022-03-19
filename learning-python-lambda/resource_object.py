import boto3


# getting aws mgmt console programatically:
aws_mag_con=boto3.session.Session(profile_name="kfsoladmin")
iam_con_re=aws_mag_con.resource(service_name="iam",region_name="us-east-1")
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-east-1")
s3_con_re=aws_mag_con.resource(service_name="s3",region_name="us-east-1")

# List all iam users
#response=iam_con_re.users.all()
#response=iam_con_re.users.limit()

#print(dir(iam_con_re.users))
#print(iam_con_re.users.all())

# for each_item in iam_con_re.users.all():
#     print(each_item)


#print(dir(iam_con_re.users.all()))

# for each_item in iam_con_re.users.all():
#     print(each_item.user_name)

# for each_item in iam_con_re.users.limit(2):
#     print(each_item.user_name)

# get bucket names


for each_item in s3_con_re.buckets.limit(1):
    print(each_item.name)
