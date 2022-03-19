import boto3
from pprint import pprint
import datetime
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
    print(dir(each_snap))
    break

    # This gives:
    # Request my snapshots with resource object
    # ec2.Snapshot(id='snap-04ad9cbfc1a8d856e')
    # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_id', 'copy', 'create_tags', 'data_encryption_key_id', 'delete', 'describe_attribute', 'description', 'encrypted', 'get_available_subresources', 'id', 'kms_key_id', 'load', 'meta', 'modify_attribute', 'outpost_arn', 'owner_alias', 'owner_id', 'progress', 'reload', 'reset_attribute', 'snapshot_id', 'start_time', 'state', 'state_message', 'tags', 'volume', 'volume_id', 'volume_size', 'wait_until_completed']
    # And as operation it gives: operation start_time in it.

for each_snap in ec2_con_re.snapshots.filter(OwnerIds=[my_own_id]):
    print(each_snap.start_time)

print("But if you want to run this script everyday and view the snapshots of that day and no older snapshots:")
today=datetime.datetime.now()
print(" type of today is",type(today))  #  type of today is <class 'datetime.datetime'>
my_start_time_request=str(datetime.datetime(today.year,today.month,8,20,50,3))
print("my requested starttime for listing snaps  is ",my_start_time_request, " type of start_time is",type(my_start_time_request))

# gives: my requested starttime for listing snaps  is  2022-03-08 20:50:03  type of start_time is <class 'str'>

print("These are all my snaps:")
for each_snap in ec2_con_re.snapshots.filter(OwnerIds=[my_own_id]):
    print(each_snap.id, each_snap.start_time.strftime("%Y-%m-%d %H:%M:%S"))
#gives
#snap-04ad9cbfc1a8d856e 2022-03-08 20:50:03
#snap-0aebd06211e1a6470 2022-03-08 20:49:36


print("These are all my snaps at my requested starttime of:",my_start_time_request)
for each_snap in ec2_con_re.snapshots.filter(OwnerIds=[my_own_id]):
    if each_snap.start_time.strftime("%Y-%m-%d %H:%M:%S")==my_start_time_request:
        print(type(each_snap.start_time.strftime("%Y-%m-%d %H:%M:%S"))) # this is a string so my_start_time_request must be stringified.
        print(each_snap.id, each_snap.start_time.strftime("%Y-%m-%d %H:%M:%S"))

# this gives:
# These are all my snaps at my requested starttime of: 2022-03-08 20:50:03
# <class 'str'>
# snap-04ad9cbfc1a8d856e 2022-03-08 20:50:03




my_start_time_request=str(datetime.datetime(today.year,today.month,8,20,49,36))
print("These are all my snaps at my requested starttime of:",my_start_time_request)
for each_snap in ec2_con_re.snapshots.filter(OwnerIds=[my_own_id]):
    if each_snap.start_time.strftime("%Y-%m-%d %H:%M:%S")==my_start_time_request:
        print(type(each_snap.start_time.strftime("%Y-%m-%d %H:%M:%S"))) # this is a string so my_start_time_request must be stringified.
        print(each_snap.id, each_snap.start_time.strftime("%Y-%m-%d %H:%M:%S"))
# gives:
# These are all my snaps at my requested starttime of: 2022-03-08 20:49:36
# <class 'str'>
# snap-0aebd06211e1a6470 2022-03-08 20:49:36


