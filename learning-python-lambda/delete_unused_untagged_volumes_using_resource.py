import boto3
aws_mag_con=boto3.session.Session(profile_name="kfsoladmin")
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-east-1")
for each_volume in ec2_con_re.volumes.all():
    print(each_volume.id, each_volume.state)
    
# gives:
# vol-09081c14f9b758685 in-use
# vol-027799c646b30338e in-use
# volume.id en vlume.state vind je in boto3 onder EC2 --> volume    


# now get only available voluems , and ot the in-use ones:

print("Show available volumes:")
# create filter:
filter_ebs_unused={"Name":"status","Values":["available"]}
for each_volume in ec2_con_re.volumes.filter(Filters=[filter_ebs_unused]):
    print(each_volume.id, each_volume.state)


print("Show available volumes + tags:")
# there is no filter showing resources that have no tags. Gebruik: if not each_volume.tags:
for each_volume in ec2_con_re.volumes.filter(Filters=[filter_ebs_unused]):
    print(each_volume.id, each_volume.state,each_volume.tags)

print("Show available volumes and are untagged:")
# there is no filter showing resources that have no tags. Gebruik: if not each_volume.tags:
for each_volume in ec2_con_re.volumes.filter(Filters=[filter_ebs_unused]):
    if not each_volume.tags:
        print(each_volume.id, each_volume.state,each_volume.tags)
        print("Deleting unused and untagged volumes...")
        #each_volume.delete()
    
print("Deleted unused and untagged volumes...")
