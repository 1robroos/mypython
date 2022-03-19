from re import M
import boto3
from pprint import pprint
import time
aws_con=boto3.session.Session(profile_name="kfsoladmin")
ec2_con_re=aws_con.resource(service_name="ec2",region_name="us-east-1")
ec2_con_cli=aws_con.client(service_name="ec2",region_name="us-east-1")
my_inst_ob=ec2_con_re.Instance("i-059335ab0f5edc2c2") #class EC2.Instance(id) 
#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#ec2
# ==> Table of Contents ==> EC2 ==> Instance
print("Starting given instances", my_inst_ob)
my_inst_ob.start()
# WITH RESOURCE OBJECT:
#my_inst_ob.wait_until_running()
        # YOUR OWN LOOP:
        # while True:
        #     my_inst_ob=ec2_con_re.Instance("i-059335ab0f5edc2c2")
        #     print("Current state is :",my_inst_ob.state['Name'])
        #     if my_inst_ob.state['Name']=="running":
        #         break
        #     print("Waiting for EC2 to get in run status")
        #     time.sleep(5)
        # print(my_inst_ob.state['Name'])
#print("Instance is now running")
#print(dir(my_inst_ob))
'''
# NOW WITH CLIENT OBJECT
print('Starting ec2 instance')
ec2_con_cli.start_instances(InstanceIds=['i-059335ab0f5edc2c2'])
waiter = ec2_con_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=['i-059335ab0f5edc2c2']) # 40 checks after every 15 seconds
print('Now ec2 i-059335ab0f5edc2c2 is running ')
'''

my_inst_ob=ec2_con_re.Instance("i-059335ab0f5edc2c2") #class EC2.Instance(id) 
print("Starting given instances", my_inst_ob)
my_inst_ob.start()
waiter = ec2_con_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=['i-059335ab0f5edc2c2']) # 40 checks after every 15 seconds
print('Now ec2 i-059335ab0f5edc2c2 is running ')

