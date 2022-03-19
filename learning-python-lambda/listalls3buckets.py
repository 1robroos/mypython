#!/home/linuxbrew/.linuxbrew/bin/python3
import boto3


# getting aws mgmt console programatically:
aws_mag_con=boto3.session.Session(profile_name="kfsoladmin")

# get s3 console
s3_con=aws_mag_con.resource('s3')  # ipv resource kan je ook client nemen )
for each_buk in s3_con.buckets.all():
    print(each_buk.name)
 # output like 969526043371-api-gateway-access   
    
print( 'and now like https://binaryguy.tech/aws/s3/list-s3-buckets-easily-using-python-and-cli/')
# s3 = boto3.client('s3')
# response = s3.list_buckets()#91;'Buckets']
# for bucket in response:
#     print('Bucket name: {}, Created on: {}'.format(bucket&#91;'Name'], bucket&#91;'CreationDate']))
                                                   
                                                   
s3 = boto3.resource('s3')
buckets = s3.buckets.all()
for bucket in buckets:
    print(bucket)                                                   
    
    # output like s3.Bucket(name='969526043371-api-gateway-access')
    