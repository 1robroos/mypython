import boto3
from pprint import pprint

session=boto3.session.Session(profile_name="kfsoladmin")
ec2_client=session.client(service_name="ec2",region_name="us-east-1")

all_regions=[]
for each_region in ec2_client.describe_regions()['Regions']:
    all_regions.append(each_region.get('RegionName'))
    
for each_region in all_regions:
    print("____________________________________________________________________")
    print("Working on region {} ".format(each_region))
    ec2_client=session.client(service_name="ec2",region_name=each_region)
    list_volume_ids=[]
    filter_prod_backup={"Name":"tag:Prod","Values":["Backup","backup"]}
    '''
    for each_volume in ec2_client.describe_volumes(Filters=[filter_prod_backup])['Volumes']:
        list_volume_ids.append(each_volume['VolumeId'])
        
    print("list of prod voluems :",list_volume_ids)
    '''

    # Paginating needed for when you have more than 50 volumes
    paginator = ec2_client.get_paginator('describe_volumes')
    response_iterator = paginator.paginate(Filter=[filter_prod_backup])
    print(response_iterator) # geeft <botocore.paginate.PageIterator object at 0x7f9e0a811f40>
    # we gaan page voor page printen:
    for each_page in paginator.paginate(Filters=[filter_prod_backup]):
        pprint(each_page['Volumes']) # Dit geeft weer een list of volumes, paginated.
        # je moet nu nog een extra loop creeren om page by page te iteraten.
        for each_volume in each_page['Volumes']:
            list_volume_ids.append(each_volume['VolumeId'])
        
    print("list of prod voluems :",list_volume_ids)
    # geeft:
    #list of prod voluems : ['vol-09081c14f9b758685', 'vol-027799c646b30338e']
    if bool(list_volume_ids)==False:
        continue

    for each_volid in list_volume_ids:
        print("Taking snap of {}".format(each_volid))
        #geeft
        #Taking snap of vol-09081c14f9b758685
        #Taking snap of vol-027799c646b30338e
        
    print("create snaps")
    snapids=[]
    for each_volid in list_volume_ids:
        response=ec2_client.create_snapshot(
                    Description="Taking snapshot with Lambda and CloudWatch",
                    VolumeId=each_volid,
                    TagSpecifications=[
                        {
                            'ResourceType':'snapshot',
                            'Tags': [
                                {
                                    'Key':'Delete-on',
                                    'Value':'90'
                                },
                                {
                                    'Key':'Name',
                                    'Value':'GOIMIJMAARWEG'
                                }
                            ]
                        }
                    ]
        )
        snapids.append((response.get('SnapshotId')))
        print("the snap ids are:",snapids)
        # print("show snap with response.get method")
        # print(response.get('SnapshotId'))
        # print("show snap with response[''] method")
        # print(response['SnapshotId'])
        
    # create a waiter.
    waiter = ec2_client.get_waiter('snapshot_completed')

    # apply the waiter:
    # filter, of onwerid of snapshot id gebruiken. Wij gebruiken nu de snapshotid's.

    waiter.wait(SnapshotIds=snapids)

    print("Snaps are created !")