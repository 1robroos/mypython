from http import client
from urllib import response
from pprint import pprint
import boto3
import sys
aws_mag_con=boto3.session.Session(profile_name="kfsoladmin")
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-east-1")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-1")
while True:
    print("This script performs the following actions on EC2 instance")
    print("""
          1. start
          2. stop
          3. terminate
          4. exit
          """)
    opt=int(input("Enter your option: "))
    if opt==1:
        print("I show you the instances:")
        my_req_instance_object=ec2_con_cli.describe_instances()['Reservations']
        for each_item in my_req_instance_object:
            for each_ec2 in each_item['Instances']:
                print(each_ec2['InstanceId'])
        print('_____________')
        instance_id=input("enter your ec2 instance id: ")
        print("Starting EC2 instance ....")
        ec2_con_cli.start_instances(InstanceIds=[instance_id])
    elif opt==2:
        print("I show you the instances and their state:")
        print('_____________')
        ec2_info=ec2_con_cli.describe_instances()['Reservations'] # request dict key 'Reservations' , it will give you a list.
        for all_ec2 in ec2_info:                                  # for all ec2 instances in that list:
            for each_ec2 in all_ec2['Instances']:                 # walk through each ec2 info
                state_dic=each_ec2['State']                       # get the State dictionary of the ec2 info # see response syntax in  https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instances
                state=state_dic['Name']                           # get the key 'Name' out of the State dictionary
                #print(type(state))                                # <class 'str'>
                print(each_ec2['InstanceId'],state)               # print instance id and its state value
        print('_____________')

        instance_id=input("enter your ec2 instance id: ")
        print("Stopping EC2 instance ....")
        ec2_con_cli.stop_instances(InstanceIds=[instance_id])
        print('_____________')        
        print("Checking the status of the instance {}\n".format(instance_id))
        that_one_ec2_machine=ec2_con_cli.describe_instances(InstanceIds=[instance_id])['Reservations']
        for my_ec2 in that_one_ec2_machine:                       # for all ec2 instances in that list:  ( only one instance )
            for each_ec2 in my_ec2['Instances']:                  # walk through each ec2 info
                state_dic=each_ec2['State']                       # get the State dictionary of the ec2 info # see response syntax in  https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instances
                state=state_dic['Name']                           # get the key 'Name' out of the State dictionary
                print(each_ec2['InstanceId'],state)               # print instance id and its state value
        print('_____________')        
    elif opt==3:
        instance_id=input("enter your ec2 instance id: ")
        my_req_instance_object=ec2_con_re.Instance(instance_id)
        print("Terminating EC2 instance ....")
        my_req_instance_object.terminate()
    elif opt==4:
        print("Thank you for using this script ")
        sys.exit()
    else:
        print("Your option is invalid, please try again")