import boto3
from pprint import pprint
aws_mag_con=boto3.session.Session(profile_name="kfsoladmin")
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-east-1")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-1")

sts_con_cli=aws_mag_con.client(service_name="sts",region_name="us-east-1")
response =sts_con_cli.get_caller_identity()
my_own_id=response.get('Account')

print("Request my snapshots with resource object")
for each_snap in ec2_con_re.snapshots.filter(OwnerIds=[my_own_id]):
    print(each_snap)
    # this gives:
        # Request my snapshots with resource object
        # ec2.Snapshot(id='snap-04ad9cbfc1a8d856e')
        # ec2.Snapshot(id='snap-0aebd06211e1a6470')
    
#now with client object:

# to much info: print(ec2_con_cli.describe_snapshots())   ==> all amazon snapshots.
# gives a list in dict: {'Snapshots': [{'Description': 'snapshot of image.vmdk', 'Encrypted': False, 'OwnerId': '099720109477', 'Progress': '100%', 'Sna
# for usage: see docs: 
# response = client.describe_snapshots(
#     Filters=[
#         {
#             'Name': 'status',
#             'Values': [
#                 'pending',
#             ],
#         },
#     ],
#     OwnerIds=[
#         '012345678910',
#     ],
# )

# print(response)

print("Request my snapshots with client object")    
response = ec2_con_cli.describe_snapshots(
    OwnerIds=[
        my_own_id
    ],
)

print(response)    
# gives:
#{'Snapshots': [{'Description': 'testsnapshot_A=B', 'Encrypted': False, 'OwnerId': '969526043371', 'Progress': '100%', 'SnapshotId': 'snap-04ad9cbfc1a8d856e', 'StartTime': datetime.datetime(2022, 3, 8, 20, 50, 3, 417000, tzinfo=tzutc()), 'State': 'completed', 'VolumeId': 'vol-09081c14f9b758685', 'VolumeSize': 8, 'Tags': [{'Key': 'Name', 'Value': 'testsnapshot_B'}]}, {'Description': 'testsnapshot_A', 'Encrypted': False, 'OwnerId': '969526043371', 'Progress': '100%', 'SnapshotId': 'snap-0aebd06211e1a6470', 'StartTime': datetime.datetime(2022, 3, 8, 20, 49, 36, 685000, tzinfo=tzutc()), 'State': 'completed', 'VolumeId': 'vol-047eb25fa2a777364', 'VolumeSize': 1, 'Tags': [{'Key': 'Name', 'Value': 'testsnapshot_A'}]}], 'ResponseMetadata': {'RequestId': '4daded20-3fe7-4a4d-be49-903dd1d51adc', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amzn-requestid': '4daded20-3fe7-4a4d-be49-903dd1d51adc', 'cache-control': 'no-cache, no-store', 'strict-transport-security': 'max-age=31536000; includeSubDomains', 'content-type': 'text/xml;charset=UTF-8', 'content-length': '1617', 'date': 'Wed, 09 Mar 2022 19:33:19 GMT', 'server': 'AmazonEC2'}, 'RetryAttempts': 0}}

for each_snapshot in response['Snapshots']:
    pprint(each_snapshot)
    # this gives with pprint: 2 dicts
        # {'Description': 'testsnapshot_A=B',
        # 'Encrypted': False,
        # 'OwnerId': '969526043371',
        # 'Progress': '100%',
        # 'SnapshotId': 'snap-04ad9cbfc1a8d856e',
        # 'StartTime': datetime.datetime(2022, 3, 8, 20, 50, 3, 417000, tzinfo=tzutc()),
        # 'State': 'completed',
        # 'Tags': [{'Key': 'Name', 'Value': 'testsnapshot_B'}],
        # 'VolumeId': 'vol-09081c14f9b758685',
        # 'VolumeSize': 8}
        # {'Description': 'testsnapshot_A',
        # 'Encrypted': False,
        # 'OwnerId': '969526043371',
        # 'Progress': '100%',
        # 'SnapshotId': 'snap-0aebd06211e1a6470',
        # 'StartTime': datetime.datetime(2022, 3, 8, 20, 49, 36, 685000, tzinfo=tzutc()),
        # 'State': 'completed',
        # 'Tags': [{'Key': 'Name', 'Value': 'testsnapshot_A'}],
        # 'VolumeId': 'vol-047eb25fa2a777364',
        # 'VolumeSize': 1}
        
for each_snapshot in response['Snapshots']:
    pprint(each_snapshot['SnapshotId'])
    # this gives:
        # 'snap-04ad9cbfc1a8d856e'
        # 'snap-0aebd06211e1a6470'
        
print("Now with client object in 2 lines:")        
for each_snapshot in ec2_con_cli.describe_snapshots(OwnerIds=[my_own_id])['Snapshots']:
    pprint(each_snapshot['SnapshotId'])