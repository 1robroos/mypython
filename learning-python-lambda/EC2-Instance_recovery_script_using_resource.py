import boto3
import csv
from pprint import pprint

aws_mag_con=boto3.session.Session(profile_name="kfsoladmin")
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-east-1")
# For fetching volume:use client object
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-1")

cnt=1
csv_ob=open("inventory_info.csv","w",newline='')
csv_w=csv.writer(csv_ob)
csv_w.writerow(["S_NO","Instance_ID","Instance_TYpe","Architecture","Launchteim","priv_ip","Volume"])
for each in ec2_con_re.instances.all():
    f1={"Name": "attachment.instance-id", "Values":[each.id]}
    for each_vol in ec2_con_cli.describe_volumes(Filters=[f1])['Volumes']:
        #print("dictionary:  ",each_vol) # this give dict
        #print("list:  ",each_vol['Attachments']) # this gives list 
        for each_att in each_vol['Attachments']:
            #print(each_att['VolumeId'])
            volumeid=each_att['VolumeId']
    print(cnt,each.instance_id,each.instance_type,each.architecture,each.launch_time.strftime("%Y-%m-%d"),each.private_ip_address,volumeid)
    csv_w.writerow([cnt,each.instance_id,each.instance_type,each.architecture,each.launch_time.strftime("%Y-%m-%d"),each.private_ip_address,volumeid])
    cnt+=1
    #print('xxxxxx')
csv_ob.close()
    
