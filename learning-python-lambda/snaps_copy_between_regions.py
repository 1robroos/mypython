import os,sys
try:
    import boto3
    print("Imported boto3 successfully")
except Exception as e:
    print(e)
    sys.exit(1)
    
source_region="us-east-1"
dest_region="us-east-2"

session=boto3.session.Session(profile_name="kfsoladmin")
ec2_source_client=session.client(service_name="ec2",region_name=source_region)

# collect your snaspshots.
# this is too mucH; all public snaps also:The snapshots available to you include public snapshots, private snapshots that you own, and private snapshots owned by other Amazon Web Services accounts for which you have explicit create volume permissions.
# for each_snap in ec2_source_client.describe_snapshots():
#     print(each_snap)


sts_client=session.client(service_name="sts",region_name="us-east-1")
account_id=sts_client.get_caller_identity().get('Account')
#for each_snap in ec2_source_client.describe_snapshots(OwnerIds=[account_id]).get('Snapshots'):
for each_snap in ec2_source_client.describe_snapshots(OwnerIds=[account_id]).get('Snapshots'):
    print(each_snap)
# Geeft:    
# Imported boto3 successfully
# {u'Description': 'Taking snapshot with Lambda and CloudWatch', u'Tags': [{u'Value': '90', u'Key': 'Delete-on'}, {u'Value': 'GOIMIJMAARWEG', u'Key': 'Name'}, {u'Value': 'yes', u'Key': 'backup'}], u'Encrypted': False, u'VolumeId': 'vol-09081c14f9b758685', u'State': 'completed', u'VolumeSize': 8, u'StartTime': datetime.datetime(2022, 3, 23, 20, 45, 15, 86000, tzinfo=tzutc()), u'Progress': '100%', u'OwnerId': '969526043371', u'SnapshotId': 'snap-0330b44b420548ee5'}
# {u'Description': 'Taking snapshot with Lambda and CloudWatch', u'Tags': [{u'Value': '90', u'Key': 'Delete-on'}, {u'Value': 'GOIMIJMAARWEG', u'Key': 'Name'}], u'Encrypted': False, u'VolumeId': 'vol-09081c14f9b758685', u'State': 'completed', u'VolumeSize': 8, u'StartTime': datetime.datetime(2022, 3, 23, 19, 17, 15, 529000, tzinfo=tzutc()), u'Progress': '100%', u'OwnerId': '969526043371', u'SnapshotId': 'snap-02ca80b47baa44c7a'}
# {u'Description': 'Taking snapshot with Lambda and CloudWatch', u'Tags': [{u'Value': 'GOIMIJMAARWEG', u'Key': 'Name'}, {u'Value': 'yes', u'Key': 'backup'}, {u'Value': '90', u'Key': 'Delete-on'}], u'Encrypted': False, u'VolumeId': 'vol-027799c646b30338e', u'State': 'completed', u'VolumeSize': 8, u'StartTime': datetime.datetime(2022, 3, 23, 20, 45, 15, 487000, tzinfo=tzutc()), u'Progress': '100%', u'OwnerId': '969526043371', u'SnapshotId': 'snap-06b2b5dbc68f6a202'}
# {u'Description': 'Taking snapshot with Lambda and CloudWatch', u'Tags': [{u'Value': '90', u'Key': 'Delete-on'}, {u'Value': 'GOIMIJMAARWEG', u'Key': 'Name'}], u'Encrypted': False, u'VolumeId': 'vol-027799c646b30338e', u'State': 'completed', u'VolumeSize': 8, u'StartTime': datetime.datetime(2022, 3, 23, 19, 17, 15, 947000, tzinfo=tzutc()), u'Progress': '100%', u'OwnerId': '969526043371', u'SnapshotId': 'snap-0a47356f991014ee2'}



# Response Syntax is een dict: die vragen we op:

# {
#     'Snapshots': [
#         {
            
print("#####################################################################################################")


# maak een filter:
filter_backuptag={"Name":"tag:backup","Values":["yes"]}
for each_snap in ec2_source_client.describe_snapshots(Filters=[filter_backuptag],OwnerIds=[account_id]).get('Snapshots'):
    print(each_snap)
    
# {u'Description': 'Taking snapshot with Lambda and CloudWatch', u'Tags': [{u'Value': '90', u'Key': 'Delete-on'}, {u'Value': 'GOIMIJMAARWEG', u'Key': 'Name'}, {u'Value': 'yes', u'Key': 'backup'}], u'Encrypted': False, u'VolumeId': 'vol-09081c14f9b758685', u'State': 'completed', u'VolumeSize': 8, u'StartTime': datetime.datetime(2022, 3, 23, 20, 45, 15, 86000, tzinfo=tzutc()), u'Progress': '100%', u'OwnerId': '969526043371', u'SnapshotId': 'snap-0330b44b420548ee5'}
# {u'Description': 'Taking snapshot with Lambda and CloudWatch', u'Tags': [{u'Value': 'GOIMIJMAARWEG', u'Key': 'Name'}, {u'Value': 'yes', u'Key': 'backup'}, {u'Value': '90', u'Key': 'Delete-on'}], u'Encrypted': False, u'VolumeId': 'vol-027799c646b30338e', u'State': 'completed', u'VolumeSize': 8, u'StartTime': datetime.datetime(2022, 3, 23, 20, 45, 15, 487000, tzinfo=tzutc()), u'Progress': '100%', u'OwnerId': '969526043371', u'SnapshotId': 'snap-06b2b5dbc68f6a202'}

# dit zijn de twee dicts met de snapshots met tag backup value yes.
# Nu enkel de snapshot id's

    
print("#####################################################################################################")

backup_snaplist=[]
filter_backuptag={"Name":"tag:backup","Values":["yes"]}
for each_snap in ec2_source_client.describe_snapshots(Filters=[filter_backuptag],OwnerIds=[account_id]).get('Snapshots'):
    print(each_snap['SnapshotId'])
    print("or")
    print(each_snap.get('SnapshotId'))
    backup_snaplist.append(each_snap.get('SnapshotId'))
    print("list is ",backup_snaplist)
    
    
if bool(backup_snaplist)==False:
    print("No candidates for snapshosts. Going to exit")
    sys.exit(1)
else:
    print("Candiditates for snaps : ",backup_snaplist)

print("#####################################################################################################")
 
# Now copy to different region. Daar moet je een object voor creeren.
#
ec2_dest_client=session.client(service_name="ec2",region_name=dest_region)


#  copy_snapshot client object:
# Request Syntax

# response = client.copy_snapshot(
#     Description='string',
#     DestinationOutpostArn='string',
#     Encrypted=True|False,
#     KmsKeyId='string',
#     SourceRegion='string',
#     SourceSnapshotId='string',
#     TagSpecifications=[
#         {
#             'ResourceType': 'capacity-reservation'|'client-vpn-endpoint'|'customer-gateway'|'carrier-gateway'|'dedicated-host'|'dhcp-options'|'egress-only-internet-gateway'|'elastic-ip'|'elastic-gpu'|'export-image-task'|'export-instance-task'|'fleet'|'fpga-image'|'host-reservation'|'image'|'import-image-task'|'import-snapshot-task'|'instance'|'instance-event-window'|'internet-gateway'|'ipam'|'ipam-pool'|'ipam-scope'|'ipv4pool-ec2'|'ipv6pool-ec2'|'key-pair'|'launch-template'|'local-gateway'|'local-gateway-route-table'|'local-gateway-virtual-interface'|'local-gateway-virtual-interface-group'|'local-gateway-route-table-vpc-association'|'local-gateway-route-table-virtual-interface-group-association'|'natgateway'|'network-acl'|'network-interface'|'network-insights-analysis'|'network-insights-path'|'network-insights-access-scope'|'network-insights-access-scope-analysis'|'placement-group'|'prefix-list'|'replace-root-volume-task'|'reserved-instances'|'route-table'|'security-group'|'security-group-rule'|'snapshot'|'spot-fleet-request'|'spot-instances-request'|'subnet'|'subnet-cidr-reservation'|'traffic-mirror-filter'|'traffic-mirror-session'|'traffic-mirror-target'|'transit-gateway'|'transit-gateway-attachment'|'transit-gateway-connect-peer'|'transit-gateway-multicast-domain'|'transit-gateway-route-table'|'volume'|'vpc'|'vpc-endpoint'|'vpc-endpoint-service'|'vpc-peering-connection'|'vpn-connection'|'vpn-gateway'|'vpc-flow-log',
#             'Tags': [
#                 {
#                     'Key': 'string',
#                     'Value': 'string'
#                 },
#             ]
#         },
#     ],
#     DryRun=True|False
# )

'''
for each_source_snapid in backup_snaplist:
    print("Taking backup for id {} into a {}".format(each_source_snapid,dest_region))
    ec2_dest_client.copy_snapshot(
        Description="Disastre REcovery",
        SourceRegion=source_region,
        SourceSnapshotId=each_source_snapid
    )
'''
# # dit geeft:
# Taking backup for id snap-0330b44b420548ee5 into a us-east-2
# Taking backup for id snap-06b2b5dbc68f6a202 into a us-east-2  
# je krijgt gelijk je prompt terug, maar de console laat nog zien dat de snap copies nog in pending staan
# dus een waiter aanmaken:

dest_snapids=[]
print("create waiter so that the script waits until the snaps are created")
for each_source_snapid in backup_snaplist:
    print("Taking backup for id {} into a {}".format(each_source_snapid,dest_region))
    response=ec2_dest_client.copy_snapshot(
        Description="Disastre REcovery",
        SourceRegion=source_region,
        SourceSnapshotId=each_source_snapid
    )
    dest_snapids.append((response.get('SnapshotId')))
    print("the copied snap ids in region {} are {}".format(dest_region,dest_snapids))
    
    
     
# create a waiter.
waiter = ec2_dest_client.get_waiter('snapshot_completed')
waiter.wait(SnapshotIds=dest_snapids)
print("Snaps are created in destionation region  {} !".format(dest_region))
print("Now modify tags for the EBS volumes in the source region for which the backup is completed.")

for each_source_snapid in backup_snaplist:
    print("Deleting old tags")
    ec2_source_client.delete_tags(
        Resources=[each_source_snapid],
        Tags=[
            {
            "Key":"backup",
            "Value":"yes"
            }
        ]
        )
    print("Create new tags")
    ec2_source_client.create_tags(
        Resources=[each_source_snapid],
        Tags=[
            {
            "Key":"backup",
            "Value":"completed"
            }
        ]
    )
    